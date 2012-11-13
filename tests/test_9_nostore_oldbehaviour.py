# vim:fileencoding=utf-8:sw=4

import os
import unittest
from base import TestBase, dbdir

config = '''\
[config]
id = id_NUMBER
lang = en
indexing = TITLE, DESCRIPTION, extra
storing =

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

badver_config = '''\
[config]
version = unknown
id = id_NUMBER
lang = en
indexing = TITLE, DESCRIPTION, extra
storing =

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

doc1 = {
    'id_NUMBER': 4,
    'TITLE': 'second',
    'DESCRIPTION': 'This is just a document for testing purpose :-)',
    'sortme': '3',
    'extra': 'some extra text',
    'n': 12,
}
doc2 = {
    'id_NUMBER': 1,
    'TITLE': 'first',
    'DESCRIPTION': 'This is just a second document for testing purpose :-)',
    'sortme': '3',
    'n': 2,
}
doc3 = {
    'id_NUMBER': 7,
    'TITLE': 'thirdd',
    'DESCRIPTION': 'This is just another document for testing purpose :-)',
    'sortme': '1',
    'n': 101,
}

class TestQuery(TestBase):
    mode = 'RDWR'
    dbname = 'test_nostore'
    def setUp(self):
        TestBase.setUp(self)

    def config(self, config):
        ans = self.client.createdb(name=self.dbname, conf=config)
        self.client.setdb(self.dbname)

    def insert_docs(self):
        ans = self.client.insert(doc1)
        self.assertEqual(ans, {u'status': u'ok'})
        ans = self.client.insert(doc2)
        self.assertEqual(ans, {u'status': u'ok'})
        ans = self.client.insert(doc3)
        self.assertEqual(ans, {u'status': u'ok'})

    def test_query(self):
        self.config(config)
        self.insert_docs()

        ans = self.client.query('title:second')
        self.assertEqual(ans['results'], [1])
        ans = self.client.query('title:second', type='_id')
        self.assertEqual(ans['results'], [1])
        ans = self.client.query('title:second', type='id')
        self.assertEqual(ans['results'], [4])
        ans = self.client.query('title:second', type='doc')
        self.assertEqual(ans['results'], [{'_id': 4}])

    def test_query_withbadver(self):
        self.config(badver_config)
        self.insert_docs()

        ans = self.client.query('title:second')
        self.assertEqual(ans['results'], [1])
        ans = self.client.query('title:second', type='_id')
        self.assertEqual(ans['results'], [1])
        ans = self.client.query('title:second', type='id')
        self.assertEqual(ans['results'], [4])
        ans = self.client.query('title:second', type='doc')
        self.assertEqual(ans['results'], [{'_id': 4}])

    def tearDown(self):
        TestBase.tearDown(self)
        os.system("rm -rf '%s'" % os.path.join(dbdir, self.dbname))
        os.unlink(os.path.join(dbdir, '%s.ini' % self.dbname))

if __name__ == '__main__':
    unittest.main()

