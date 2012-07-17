# vim:fileencoding=utf-8:sw=4

import json
import struct
from ConfigParser import RawConfigParser

def parse_netint(b):
    return struct.unpack('!I', b)[0]

def pack_netint(i):
    return struct.pack('!I', i)

def fromjson(s):
    return json.loads(s, encoding='utf-8')

def tojson(d):
    return json.dumps(d, ensure_ascii=False).encode('utf-8')

def write_response(fp, s):
    if isinstance(s, dict):
        s = tojson(s)
    fp.write(pack_netint(len(s)))
    fp.write(s)
    fp.flush()

def read_response(fp):
    r = fp.read(4)
    if not r:
        return

    length = parse_netint(r)
    got = 0
    data = []
    while got < length:
        r = fp.read(length - got)
        if not r:
            return
        got += len(r)
        data.append(r)

    return fromjson(''.join(data))

class CasedConfigParser(RawConfigParser):
    def optionxform(self, option):
        return option

