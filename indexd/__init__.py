# vim:fileencoding=utf-8:sw=4

import json
import logging

from gevent.server import StreamServer

from exceptions import *
from request import Request
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

class IndexServer(object):
    def __init__(self, address):
        self._server = StreamServer(address, Connection)

    def start(self):
        logger.info('IndexServer started.')
        self._server.serve_forever()

class Connection(object):
    indexdb = None
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
        try:
            d = getattr(self, method)(req)
            if 'status' not in d:
                d['status'] = 'ok'
            self.reply(d)
        except AttributeError:
            raise AWIPClientError('No such request command')

    def reply(self, json):
        logger.debug('%r: Sending reply: %r', self.addr, json)
        util.write_response(self.fp, json)

    def handle_cmd_ping(self, req):
        return {}

    def handle_cmd_set(self, req):
        name = req.name
        if name == 'indexdb':
            self.indexdb = req.get_string('value')
        return {}
