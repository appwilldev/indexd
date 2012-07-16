# vim:fileencoding=utf-8:sw=4

import unittest
from base import TestBase

class TestDB(TestBase):
    def test_setok(self):
        ans = self.client.set(name='indexdb', value='db')
        self.assertEqual(ans['status'], u'ok', 'Got %r' % ans)

    def test_setbad(self):
        ans = self.client.set(name='indexdb', value='db_nonexistent')
        self.assertMessageFind(ans, 'no such file or directory')

if __name__ == '__main__':
    unittest.main()

