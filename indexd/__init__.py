# vim:fileencoding=utf-8:sw=4

import json
import logging

from gevent.server import StreamServer

from exceptions import *
from util import *

LINE_MAX = 1024
logger = logging.getLogger(__name__)

def check_protocol(line):
    try:
        protocol, mode = line.rstrip().split(' ', 1)
    except ValueError:
        raise AWIPHandshakeFailed(line)

    if protocol != 'AWIP/01':
        raise AWIPHandshakeFailed(line)

    return protocol, mode

class IndexServer(object):
    def __init__(self, address):
        self._server = StreamServer(address, Connection)

    def start(self):
        logger.info('IndexServer started.')
        self._server.serve_forever()

class Connection(object):
    def __init__(self, socket, address):
        logger.info('New connection from %r', address)
        self.addr = address
        self.fp = socket.makefile()
        try:
            self.do_handshake()
        except AWIPClinetError, e:
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
                self.reply(e.tojson())

    def do_handshake(self):
        line = self.fp.readline(LINE_MAX)
        logger.debug('%r: Got handshake line: %r', self.addr, line)
        self.protocol, self.mode = check_protocol(line)
        self.reply('{"status": "ok"}')
        logger.info('%r: Handshake complete, protocol=%s, mode=%s', self.addr,
                    self.protocol, self.mode)

    def handle_request(self):
        req = self.parse_request()
        logger.debug('%r: Got request: %r', self.addr, req)
        if req is None:
            raise AWIPClientDisconnected
        try:
            tp = req['cmd']
        except KeyError:
            raise AWIPClinetError('No request cmd specified')
        method = 'handle_cmd_%s' % tp
        try:
            d = getattr(self, method)(req)
            if 'status' not in d:
                d['status'] = 'ok'
            self.reply(json.dumps(d, ensure_ascii=False).encode('utf-8'))
        except AttributeError:
            raise AWIPClinetError('No such request commandd')

    def reply(self, json):
        logger.debug('%r: Sending reply: %r', self.addr, json)
        self.fp.write(pack_netint(len(json)))
        self.fp.write(json)
        self.fp.flush()

    def parse_request(self):
        r = self.fp.read(4)
        if not r:
            return

        length = parse_netint(r)
        got = 0
        data = []
        while got < length:
           r = self.fp.read(length - got)
           if not r:
               return
           got += len(r)
           data.append(r)

        return json.loads(''.join(data), encoding='utf-8')

    def handle_cmd_ping(self, req):
        return {}
