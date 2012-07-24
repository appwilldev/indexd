#!/usr/bin/env python
# vim:fileencoding=utf-8:sw=4

import sys
import os
import csv
import time

thisDir = os.path.split(__file__)[0]
config = '''\
[config]
id = review_id
lang = zh
indexing = content, reviewer, title

[field_prefix]
S = title
U = reviewer

[prefix_name]
S = title
U = reviewer
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

def parse_csv_file(datapath):
    with open(datapath) as fd:
        reader = csv.DictReader(fd, delimiter='@')
        for row in reader:
            yield dict2unicode(row, 'utf-8')

def main(addr, filepath):
    print time.time(), 'import begin.'
    client = indexd.client.Client(addr)
    client.setmode('RDWR')
    print time.time(), 'creating database...'
    client.createdb(name='test_comments', conf=config)
    client.setdb('test_comments')

    print time.time(), 'start indexing...'
    for i, d in enumerate(parse_csv_file(filepath)):
        client.insert(d)
        if i % 20000 == 19999:
            client.commit()

    print time.time(), 'indexing finished.'
    client.close()
    print time.time(), 'all done.'

if __name__ == '__main__':
    # 7998748 条记录, 32140s, 40.18s/万条
    main(('', 4002), '/Users/appwillmini8/src/data/commens.csv')
