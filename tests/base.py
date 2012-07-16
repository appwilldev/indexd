# vim:fileencoding=utf-8:sw=4

import sys
import os
thisDir = os.path.split(__file__)[0]

def thisdir(p):
    return os.path.join(thisDir, p)

sys.path.append(thisdir('..'))

import subprocess
import unittest

from indexd import client

class TestBase(unittest.TestCase):
    def setUp(self):
        self.subp = subprocess.Popen(thisdir('runserver'), stderr=open(thisdir('server.log'), 'a'))
        self.client = client.Client(('', 4000))

    def tearDown(self):
        self.subp.send_signal(2)
        self.subp.wait()

if __name__ == '__main__':
    unittest.main()
