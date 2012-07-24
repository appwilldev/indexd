#!/usr/bin/env python
# vim:fileencoding=utf-8:sw=4

import sys
import os
import pipes
from pprint import pprint

thisDir = os.path.split(__file__)[0]
def thisdir(p):
    return os.path.join(thisDir, p)

dbdir = thisdir('..')
sys.path.append(dbdir)

import indexd.client

def query(q):
    ic = indexd.client.Client(('', 4002))
    ic.setmode('RDONLY')
    ic.setdb('test_comments')
    t = pipes.Template()
    t.append('ascii2uni -a U', '--')
    t.append('less -R', '--')
    pprint([x for x in ic.get(ic.query(q)['results'])['results']], t.open('/dev/stdout', 'w'))

if __name__ == '__main__':
    query(' '.join(sys.argv[1:]))
