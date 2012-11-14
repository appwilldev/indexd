# vim:fileencoding=utf-8:sw=4

import unittest
from base import TestBase

class TestDB(TestBase):
    def test_setbad(self):
        ans = self.client.setdb('db_nonexistent')
        self.assertMessageFind(ans, 'no such file or directory')

if __name__ == '__main__':
    unittest.main()

