# vim:fileencoding=utf-8:sw=4

import os
import unittest
from base import TestBase, dbdir, config

class TestCreateReadOnly(TestBase):
    def test_create_with_readonly_mode(self):
        ans = self.client.createdb('test', conf=config)
        self.assertEqual(ans['status'], u'error')

class TestCreateFailure(TestBase):
    mode = 'RDWR'
    def test_bad_createdb(self):
        ans = self.client.do_cmd('createdb')
        self.assertMessageFind(ans, 'name')

    def test_baddbname(self):
        ans = self.client.createdb(name='test-not-valid', conf=config)
        self.assertMessageFind(ans, 'database name')

        ans = self.client.createdb(name=':isReserved', conf=config)
        self.assertMessageFind(ans, 'database name')

    def test_noconf(self):
        ans = self.client.do_cmd('createdb', name='test')
        self.assertMessageFind(ans, 'confdata')

    def test_badconf(self):
        ans = self.client.createdb(name='test', conf=123)
        self.assertMessageFind(ans, 'invalid config')

        ans = self.client.createdb(name='test', conf=['abc', 'def'])
        self.assertMessageFind(ans, 'invalid config')

        ans = self.client.createdb(name='test', conf=dict(test='failure'))
        self.assertMessageFind(ans, 'invalid config')

    def test_existing(self):
        ans = self.client.createdb(name='db', conf=config)
        self.assertMessageFind(ans, 'already exist')

class TestCreateOK(TestBase):
    mode = 'RDWR'
    dbname = 'test'
    def test_create(self):
        ans = self.client.createdb(name=self.dbname, conf=config)
        self.assertEqual(ans, {u'status': u'ok'})

    def tearDown(self):
        super(TestCreateOK, self).tearDown()
        os.system("rm -rf '%s'" % os.path.join(dbdir, self.dbname))
        os.unlink(os.path.join(dbdir, '%s.ini' % self.dbname))

if __name__ == '__main__':
    unittest.main()

