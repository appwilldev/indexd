# vim:fileencoding=utf-8:sw=4

import json
import logging
import functools
import ConfigParser
import io

from gevent.server import StreamServer

from exceptions import *
from request import Request
import xapiandb
import util

LINE_MAX = 1024
logger = logging.getLogger(__name__)
supported_modes = ('RDONLY', 'RDWR')

def check_protocol(line):
    try:
        protocol, mode = line.rstrip().split(' ', 1)
    except ValueError:
        raise AWIPHandshakeFailed(line)

    if protocol != 'AWIP/01':
        raise AWIPHandshakeFailed(line)
    if mode not in supported_modes:
        raise AWIPHandshakeFailed(line, 'Bad mode')

    return protocol, mode

def indexdb_set(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.indexdb:
            raise AWIPRequestInvalid('Please set indexdb first')
        return func(self, *args, **kwargs)
    return wrapper


def conn_writable(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.mode != 'RDWR':
            raise AWIPRequestInvalid('Connection is in readonly mode')
        return func(self, *args, **kwargs)
    return wrapper


class IndexServer(object):
    def __init__(self, address):
        self._server = StreamServer(address, Connection)

    def start(self):
        logger.info('IndexServer started.')
        self._server.serve_forever()

class Connection(object):
    indexdb = None
    mode = None
    def __init__(self, socket, address):
        logger.info('New connection from %r', address)
        self.addr = address
        self.fp = socket.makefile()
        try:
            self.do_handshake()
        except AWIPClientError, e:
            logger.warn('%r: Bad Handshake line: %r', self.addr, e.line)
            self.fp.write(str(e) + '\r\n')
            self.fp.close()
            socket.close()
            return

        while True:
            try:
                self.handle_request()
            except AWIPClientDisconnected:
                if self.indexdb and self.mode == 'RDWR':
                    self.indexdb.close()
                logger.info('%r: disconnected', self.addr)
                break
            except AWIPError, e:
                logger.warn('%r: Exception', self.addr, exc_info=True)
                self.reply(e.todict())

    def do_handshake(self):
        line = self.fp.readline(LINE_MAX)
        logger.debug('%r: Got handshake line: %r', self.addr, line)
        self.protocol, self.mode = check_protocol(line)
        self.reply('200 OK\r\n')
        logger.info('%r: Handshake complete, protocol=%s, mode=%s', self.addr,
                    self.protocol, self.mode)

    def handle_request(self):
        sreq = util.read_response(self.fp)
        logger.debug('%r: Got request: %r', self.addr, sreq)
        if sreq is None:
            raise AWIPClientDisconnected
        req = Request(sreq)
        method = 'handle_cmd_%s' % req.cmd
        logger.info('%r: %s', self.addr, method)
        f = getattr(self, method, None)
        if f is None:
            raise AWIPClientError('No such request command')
        d = f(req)
        if 'status' not in d:
            d['status'] = 'ok'
        self.reply(d)

    def reply(self, json):
        logger.debug('%r: Sending reply: %r', self.addr, json)
        util.write_response(self.fp, json)

    def handle_cmd_ping(self, req):
        return {}

    def handle_cmd_set(self, req):
        name = req.name
        if name == 'indexdb':
            self.indexdb = xapiandb.get_db(req.get_string('value'), mode=self.mode)
        else:
            raise AWIPRequestInvalid('No such setting')
        return {}

    @indexdb_set
    def handle_cmd_query(self, req):
        results = self.indexdb.query(req.qs, req.start, req.size)
        d = [doc.docid for doc in results]
        return { 'results': d }

    @indexdb_set
    def handle_cmd_retrieve(self, req):
        ret = []
        for id in req.ids:
            try:
                doc = self.indexdb.get_document(id)
                ret.append(util.fromjson(doc.get_data()))
            except:
                logger.warn('%r: Exception when retrieving doc %r', self.addr, id, exc_info=True)
                ret.append(None)
        return {
            'status': 'ok',
            'results': ret,
        }

    @conn_writable
    def handle_cmd_createdb(self, req):
        name = req.name
        confdata = req.confdata
        conf = util.CasedConfigParser()
        try:
            conf.readfp(io.StringIO(confdata))
        except (ConfigParser.Error, TypeError), e:
            raise AWIPRequestInvalid('Invalid config data')
        xapiandb.createdb(name, confdata)
        return {}

    @indexdb_set
    @conn_writable
    def handle_cmd_insert(self, req):
        self.indexdb.add_document(req.document)
        return {}

    @indexdb_set
    @conn_writable
    def handle_cmd_delete(self, req):
        ret = []
        for id in req.ids:
            if isinstance(id, basestring):
                id = u'Q' + id
            try:
                self.indexdb.delete_document(id)
                ret.append(True)
            except:
                logger.warn('%r: Exception when deleting doc %r', self.addr, id, exc_info=True)
                ret.append(False)
        return {
            'status': 'ok',
            'results': ret,
        }

    @indexdb_set
    @conn_writable
    def handle_cmd_edit(self, req):
        id = req.id
        try:
            doc = self.indexdb.get_document(id)
            docdata = util.fromjson(doc.get_data())
        except Exception, e:
            logger.warn('%r: Exception when retrieving doc %r', self.addr, id, exc_info=True)
            raise AWIPRequestInvalid('failed to read the doc: ' + str(e))

        try:
            new = req.get_dict('set')
            docdata.update(new)
        except AWIPRequestInvalid:
            pass

        try:
            todel = req.get_list('del')
            for i in todel:
                try:
                    del docdata[i]
                except KeyError:
                    pass
        except AWIPRequestInvalid:
            pass

        self.indexdb.add_document(docdata)
        return {}
