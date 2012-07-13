# vim:fileencoding=utf-8:sw=4

import socket
import json
from pprint import pprint

from util import read_response, write_response

def decode_reply(re):
    return json.loads(re, encoding='utf-8')

def print_reply(re):
    if isinstance(re, str):
        re = decode_reply(re)
    pprint(re)

class Client(object):
    def __init__(self, addr):
        sock = self.sock = socket.socket()
        sock.connect(addr)
        sock.send('AWIP/01 RDONLY\r\n')
        re = sock.recv(1024)
        print re
        self.fp = sock.makefile()

    def ping(self):
        self.do_cmd('ping')

    def set(self, **kv):
        self.do_cmd('set', **kv)

    def do_cmd(self, cmd, **other):
        d = { 'cmd': cmd }
        d.update(other)
        write_response(self.fp, d)
        print_reply(read_response(self.fp))

