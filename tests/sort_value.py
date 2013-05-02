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
#print c.insert({"fullname":123, "title":"b","content":"e", "s":1, "ss":2,"sss":3})
#print c.insert({"fullname":124, "title":"b","content":"d", "s":2, "ss":1,"sss":2})
#print c.insert({"fullname":125, "title":"b","content":"c121_de", "s":3, "ss":3,"sss":1})
print c.query(u"恭喜你获得6元兑换，码 and title:你们都去死吧 and -让他们走吧", type="id")
#time.sleep(20)
