# vim:fileencoding=utf-8:sw=4

import logging
import functools

from gevent.server import StreamServer

from exceptions import *
from request import Request
import xapiandb
import util
from constants import *

logger = logging.getLogger(__name__)

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
    def __init__(self, address, modes_to_accept=supported_modes):
        self._server = StreamServer(
            address,
            functools.partial(Connection, modes_to_accept=modes_to_accept),
        )

    def start(self):
        logger.info('IndexServer started.')
        self._server.serve_forever()

class Connection(object):
    indexdb = None
    mode = None
    def __init__(self, socket, address, modes_to_accept=supported_modes):
        self.modes_to_accept = modes_to_accept
        logger.info('New connection from %r', address)
        self.addr = address
        self.sock = socket
        try:
            self.do_handshake()
        except AWIPClientError, e:
            logger.warn('%r: Bad Handshake: %r', self.addr, e.initial)
            socket.close()
            return

        try:
            self.handle_request(expect_cmd='setmode')
        except AWIPClientDisconnected, e:
            logger.info('%r: %s', self.addr, e)
            return
        except AWIPError, e:
            logger.warn('%r: Exception', self.addr, exc_info=True)
            socket.close()
            return

        while True:
            try:
                self.handle_request()
            except AWIPClientDisconnected, e:
                if self.indexdb and self.mode == 'RDWR':
                    self.indexdb.close()
                logger.info('%r: %s', self.addr, e)
                break
            except AWIPError, e:
                logger.warn('%r: Exception', self.addr, exc_info=True)
                self.reply(e.todict())

    def do_handshake(self):
        initial = util.recvbytes(self.sock, len(INITIAL_BYTES))
        self.sock.sendall(INITIAL_OK)
        logger.info('%r: Handshake complete', self.addr)

    def handle_request(self, expect_cmd=None):
        try:
            sreq = util.read_response(self.sock)
        except UnicodeDecodeError:
            logger.warn('%r: client is sending garbage!', self.addr, exc_info=True)
            raise AWIPRequestInvalid('bad encoded data')

        logger.debug('%r: Got request: %r', self.addr, sreq)
        if sreq is None:
            raise AWIPClientDisconnected
        req = Request(sreq)

        if expect_cmd and req.cmd != expect_cmd:
            raise AWIPRequestInvalid('Please set mode first')

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
        util.write_response(self.sock, json)

    def handle_cmd_ping(self, req):
        return {}

    def handle_cmd_setdb(self, req):
        self.indexdb = xapiandb.get_db(req.get_string('value'), mode=self.mode)
        return {}

    def handle_cmd_setmode(self, req):
        v = req.value
        if v in self.modes_to_accept:
            self.mode = v
        else:
            raise AWIPRequestInvalid('Unsupported mode %s' % v)
        return {}

    @indexdb_set
    def handle_cmd_query(self, req):
        results = self.indexdb.query(req.qs, req.start, req.size)
        d = [doc.docid for doc in results]
        return { 'results': d }

    @indexdb_set
    def handle_cmd_get(self, req):
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
        xapiandb.createdb(name, confdata)
        return {}

    @indexdb_set
    @conn_writable
    def handle_cmd_insert(self, req):
        self.indexdb.add_document(req.get_dict('document'))
        return {}

    @indexdb_set
    @conn_writable
    def handle_cmd_commit(self, req):
        self.indexdb.commit()
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
    def handle_cmd_update(self, req):
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
