# vim:fileencoding=utf-8

import struct

def parse_netint(b):
  return struct.unpack('!I', b)[0]

def pack_netint(i):
  return struct.pack('!I', i)
