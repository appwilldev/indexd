# vim:fileencoding=utf-8:sw=4

import json
import struct
from ConfigParser import ConfigParser

def parse_netint(b):
    return struct.unpack('!I', b)[0]

def pack_netint(i):
    return struct.pack('!I', i)

def write_response(fp, s):
    if isinstance(s, dict):
        s = json.dumps(s, ensure_ascii=False).encode('utf-8')
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

    return json.loads(''.join(data), encoding='utf-8')

class CasedConfigParser(ConfigParser):
    def optionxform(self, option):
        return option

