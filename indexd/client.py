# vim:fileencoding=utf-8:sw=4

import socket
import ujson as json
from pprint import pprint

from util import read_response, write_response, recvbytes
from constants import *

class Client(object):
    def __init__(self, addr):
        sock = self.sock = socket.socket()
        sock.connect(addr)
        sock.send(INITIAL_BYTES)
        recvbytes(sock, len(INITIAL_OK))

    def close(self):
        self.sock.close()

    def ping(self):
        return self.do_cmd('ping')

    def setmode(self, mode):
        return self.do_cmd('setmode', value=mode)

    def setdb(self, db):
        return self.do_cmd('setdb', value=db)

    def query(self, qs):
        return self.do_cmd('query', qs=qs, start=0, size=20)

    def createdb(self, name, conf):
        return self.do_cmd('createdb', name=name, confdata=conf)

    def get(self, ids):
        ids = list(ids)
        return self.do_cmd('get', ids=ids)

    def insert(self, doc):
        return self.do_cmd('insert', document=doc)

    def delete(self, ids):
        ids = list(ids)
        return self.do_cmd('delete', ids=ids)

    def update(self, id, d):
        return self.do_cmd('update', id=id, **d)

    def do_cmd(self, cmd, **other):
        d = { 'cmd': cmd }
        d.update(other)
        write_response(self.sock, d)
        return read_response(self.sock)

