#!/usr/bin/env python
# vim:fileencoding=utf-8:sw=4

import sys
import os
import csv
import time

thisDir = os.path.split(__file__)[0]
config = '''\
[config]
id = id_NUMBER
lang = en
indexing = TITLE, DESCRIPTION

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

def thisdir(p):
    return os.path.join(thisDir, p)

dbdir = thisdir('..')
sys.path.append(dbdir)

import indexd.client

def dict2unicode(d, charset='utf-8'):
    new = {}
    for k, v in d.items():
        if isinstance(k, str):
            k = k.decode(charset)
        else:
            raise ValueError("don't know how to decode type '%s'" % k.__class__.__name__)
        if isinstance(v, str):
            v = v.decode(charset)
        elif isinstance(v, dict):
            v = dict2unicode(v, charset=charset)
        else:
            raise ValueError("don't know how to decode type '%s'" % v.__class__.__name__)
        new[k] = v

    return new

def parse_csv_file(datapath, charset='iso-8859-1'):
    with open(datapath) as fd:
        reader = csv.DictReader(fd)
        for row in reader:
            yield dict2unicode(row, charset)

def main(addr, filepath):
    print time.time(), 'import begin.'
    client = indexd.client.Client(addr)
    client.setmode('RDWR')
    print time.time(), 'creating database...'
    client.createdb(name='test_en', conf=config)
    client.setdb('test_en')

    print time.time(), 'start indexing...'
    for d in parse_csv_file(filepath):
        client.insert(d)

    print time.time(), 'indexing finished.'
    client.close()
    print time.time(), 'all done.'

if __name__ == '__main__':
    # 15.7s/万
    main(('', 4002), '/Users/appwillmini8/tmpfs/NMSI_object1_20110304.csv')
