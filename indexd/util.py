# vim:fileencoding=utf-8:sw=4

import json
import struct
from ConfigParser import RawConfigParser

from exceptions import *

def parse_netint(b):
    return struct.unpack('!I', b)[0]

def pack_netint(i):
    return struct.pack('!I', i)

def recvbytes(sock, length):
    got = 0
    data = []
    while got < length:
        r = sock.recv(length - got)
        if not r:
            return
        got += len(r)
        data.append(r)
    return ''.join(data)

def fromjson(s):
    return json.loads(s, encoding='utf-8')

def tojson(d):
    return json.dumps(d, ensure_ascii=False)

def write_response(sock, s):
    if isinstance(s, dict):
        s = tojson(s)
    sock.sendall(pack_netint(len(s)))
    sock.sendall(s)

def read_response(sock):
    r = recvbytes(sock, 4)
    if not r:
        return

    length = parse_netint(r)
    data = recvbytes(sock, length)
    if data is None:
        raise AWIPClientDisconnected('client disappeared suddenly')
    return fromjson(data)

class CasedConfigParser(RawConfigParser):
    def optionxform(self, option):
        return option

