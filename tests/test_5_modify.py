# vim:fileencoding=utf-8:sw=4

import os
import unittest
from base import TestBase, dbdir, config

doc = {
    'id_NUMBER': 8237,
    'TITLE': 'test hehe',
    'DESCRIPTION': 'This is just a document for testing purpose :-)',
    'extra': 'some extra text',
}
doc2 = {
    'id_NUMBER': 8237,
    'TITLE': 'changed title',
    'DESCRIPTION': 'This is just a document for testing purpose :-)',
    'extra': 'some extra text',
}

class TestCreateInsert(TestBase):
    mode = 'RDWR'
    dbname = 'test_insert'
    def setUp(self):
        TestBase.setUp(self)
        ans = self.client.createdb(name=self.dbname, conf=config)
        self.client.setdb(self.dbname)

    def test_add_missingkey(self):
        ans = self.client.insert({'abc': 'def'})
        self.assertMessageFind(ans, 'missing key')

    def test_add_ok(self):
        ans = self.client.insert(doc)
        self.assertEqual(ans, {u'status': u'ok'})

    def test_querydb(self):
        self.test_add_ok()
        ans = self.client.query('test')
        self.assertEqual(ans['results'], [1])
        ans = self.client.get([1])['results'][0]
        self.assertEqual(ans, doc)

    def test_delete_by_id(self):
        self.test_add_ok()
        ans = self.client.delete([1])
        self.assertEqual(ans['results'], [True])
        ans = self.client.query('test')
        self.assertEqual(ans['results'], [])

    def test_delete_by_term(self):
        self.test_add_ok()
        ans = self.client.delete(["8237"])
        self.assertEqual(ans['results'], [True])
        ans = self.client.query('test')
        self.assertEqual(ans['results'], [])

    def test_delete_nonexistent(self):
        ans = self.client.delete(["8237", 32, 1])
        self.assertEqual(ans['results'], [True, False, False])

    def test_update_title_change(self):
        self.test_add_ok()
        ans = self.client.update("8237", {
            "set": {
                "TITLE": "changed title",
            }
        })
        self.assertEqual(ans, {u'status': u'ok'})
        ans = self.client.query('changing')
        self.assertEqual(ans['results'], [1])
        ans = self.client.get([1])['results'][0]
        self.assertEqual(ans, doc2)

    def test_update_title_del(self):
        self.test_add_ok()
        ans = self.client.query('extra')
        self.assertEqual(ans['results'], [1])

        ans = self.client.update(1, {
            "del": ["extra", "nonexistent"],
        })
        self.assertEqual(ans, {u'status': u'ok'})
        ans = self.client.query('extra')
        self.assertEqual(ans['results'], [])

    def tearDown(self):
        TestBase.tearDown(self)
        os.system("rm -rf '%s'" % os.path.join(dbdir, self.dbname))
        os.unlink(os.path.join(dbdir, '%s.ini' % self.dbname))

if __name__ == '__main__':
    unittest.main()

