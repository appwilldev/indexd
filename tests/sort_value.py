#-*- encoding: utf-8 -*-
import os
import sys
import time
thisDir = os.path.split(__file__)[0]

def thisdir(p):
    return os.path.join(thisDir, p)

dbdir = thisdir('..')
sys.path.append(dbdir)

from indexd import client

c = client.Client(('', 4040))
c.setmode("RDWR")
print c.ping()
print c.setdb("link")
#print c.createdb("testdb", None)
print c.insert({"fullname":123, "title":"b","text":"美国你们区和他们帐号", "author":"1", "tags":"2","ups":3})
print c.insert({"fullname":124, "title":"b","text":"美国哈哈不是的新闻帐号不是已经死了么卧室你们诗歌词语以外海南搜到么你们区", "s":2, "ss":1,"ups":2})
print c.insert({"fullname":125, "title":"b","text":"c121_de", "s":3, "ss":3,"ups":1})
print c.query(u"帐号 OR tags:xy", type="id")
#time.sleep(20)
