# vim:fileencoding=utf-8:sw=4

import socket
import json
from pprint import pprint

from util import read_response, write_response

class Client(object):
    def __init__(self, addr, mode):
        sock = self.sock = socket.socket()
        sock.connect(addr)
        sock.send('AWIP/01 %s\r\n' % mode)
        re = sock.recv(1024)
        self.fp = sock.makefile()

    def ping(self):
        return self.do_cmd('ping')

    def set(self, **kv):
        return self.do_cmd('set', **kv)

    def query(self, qs):
        return self.do_cmd('query', qs=qs, start=0, size=20)

    def createdb(self, name, conf):
        return self.do_cmd('createdb', name=name, confdata=conf)

    def retrieve(self, ids):
        ids = list(ids)
        return self.do_cmd('retrieve', ids=ids)

    def insert(self, doc):
        return self.do_cmd('insert', document=doc)

    def do_cmd(self, cmd, **other):
        d = { 'cmd': cmd }
        d.update(other)
        write_response(self.fp, d)
        return read_response(self.fp)

