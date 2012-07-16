# vim:fileencoding=utf-8:sw=4

import unittest
from base import TestBase

class TestPing(TestBase):
    def test_ping(self):
        self.assertEqual(self.client.ping(), {u'status': u'ok'})

if __name__ == '__main__':
  unittest.main()


