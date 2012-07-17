# vim:fileencoding=utf-8:sw=4

import sys
import os

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

import time
import subprocess
import unittest

from indexd import client

class TestBase(unittest.TestCase):
    mode = 'RDONLY'
    maxDiff = None
    def setUp(self):
        self.subp = subprocess.Popen(thisdir('runserver'), stderr=open(thisdir('server.log'), 'a'))
        time.sleep(0.5)
        self.client = client.Client(('', 4000), self.mode)

    def tearDown(self):
        self.subp.send_signal(2)
        self.subp.wait()

    def assertMessageFind(self, ans, phrase):
        self.assertEqual(ans['status'], u'error', 'Expected error not appear')
        self.assertTrue(ans['message'].lower().find(phrase) >= 0, "Error massage doesn't match: " + ans['message'])

if __name__ == '__main__':
    unittest.main()
