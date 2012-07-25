#!/usr/bin/env python
# vim:fileencoding=utf-8:sw=4

import sys
import os
import csv
import time

thisDir = os.path.split(__file__)[0]
config = '''\
[config]
id = app_id
lang = zh
indexing = copyright, description, developer, language, title, seller
sorting = number:all_version_rating_float, number:all_version_ratings_count, category, \
  number:current_version_rating_float, number:current_version_ratings_count, developer, language

[field_prefix]
C = copyright
XD = description
D = developer
L = language
T = title
S = seller

[prefix_name]
C = copyright
XD = description
D = developer
L = language
T = title
S = seller
'''

fields = (
    "id",
    "app_id",
    "lang",
    "store_code",
    "store_country",
    "desc_lang",
    "app_url",
    "title",
    "developer",
    "developer_itunes_link",
    "developer_id",
    "description",
    "developer_url",
    "whatsnew",
    "screenshot_links",
    "screenshot_links_ipad",
    "app_icon",
    "price",
    "category",
    "release_date",
    "current_version",
    "current_version_verbose",
    "size",
    "language",
    "seller",
    "copyright",
    "app_rating",
    "requirement",
    "current_version_rating",
    "current_version_rating_float",
    "current_version_ratings_count",
    "all_version_rating",
    "all_version_rating_float",
    "all_version_ratings_count",
    "both_for_iphone_ipad",
    "only_for_ipad",
    "game_center",
    "has_iap",
    "status",
    "update_time",
    "fetch_time",
    "app_sig",
)

def thisdir(p):
    return os.path.join(thisDir, p)

dbdir = thisdir('..')
sys.path.append(dbdir)

import indexd.client

N = 778011
file = '/home/lilydjwg/data/apps_non_us_store.txt'

def read_from_file(file):
    with open(file) as f:
        for line in f:
            if line.endswith('\\\n'):
                line = line[:-2] + f.readline()[:-1]
            else:
                line = line[:-1]
            yield dict(zip(fields, line.split('@@@')))

def main():
    print time.time(), 'Starting...'
    ic = indexd.client.Client(('', 4002))
    ic.setmode('RDWR')
    ic.createdb('app_store', config)
    ic.setdb('app_store')

    lastt = time.time()
    print lastt, '%d docuemts...Ready to go!' % N
    try:
        for i, data in enumerate(read_from_file(file)):
            # avoid those bad data will kill the connection
            if data['description'] != r'\N':
                del data['id']
                ret = ic.insert(data)
                assert ret['status'] == 'ok', ret['message']
            if i and i % 2000 == 0:
                ic.commit()
                print '%7.2f: %8d/%d done.' % (time.time() - lastt, i, N)
                lastt = time.time()
    except AssertionError:
        from cli import repl
        repl(locals())

if __name__ == '__main__':
    main()
