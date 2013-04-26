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
print c.setdb("test")
#print c.createdb("testdb", None)
#print c.insert({"fullname":123, "title":"b","content":"e", "s":1, "ss":2,"sss":3})
#print c.insert({"fullname":124, "title":"b","content":"d", "s":2, "ss":1,"sss":2})
#print c.insert({"fullname":125, "title":"b","content":"c", "s":3, "ss":3,"sss":1})
print c.query("title:b", type="id", sort=[['ss',False],["sss",False]])
#time.sleep(20)
