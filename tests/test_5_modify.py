# vim:fileencoding=utf-8:sw=4

import os
import unittest
from base import TestBase, dbdir, config

class TestCreateInsert(TestBase):
    mode = 'RDWR'
    dbname = 'test_insert'
    def setUp(self):
        super(TestCreateInsert, self).setUp()
        ans = self.client.createdb(name=self.dbname, conf=config)
        self.client.set(name='indexdb', value=self.dbname)

    def test_add_missingkey(self):
        ans = self.client.insert({'abc': 'def'})
        self.assertMessageFind(ans, 'missing key')

    def test_add_ok(self):
        ans = self.client.insert({
            'id_NUMBER': 8237,
            'TITLE': 'test hehe',
            'DESCRIPTION': 'This is just a document for testing purpose :-)',
        })
        self.assertEqual(ans, {u'status': u'ok'})

    def test_querydb(self):
        self.test_add_ok()
        ans = self.client.query('test')
        self.assertTrue(ans['results'])

    def tearDown(self):
        os.system("rm -rf '%s'" % os.path.join(dbdir, self.dbname))
        os.unlink(os.path.join(dbdir, '%s.ini' % self.dbname))
        super(TestCreateInsert, self).tearDown()

if __name__ == '__main__':
    unittest.main()

