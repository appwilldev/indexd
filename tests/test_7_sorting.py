# vim:fileencoding=utf-8:sw=4

import os
import unittest
from base import TestBase, dbdir

config = '''\
[config]
id = id_NUMBER
lang = en
indexing = TITLE, DESCRIPTION, extra
sorting = id_NUMBER, TITLE, sortme

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
}
doc2 = {
    'id_NUMBER': 1,
    'TITLE': 'first',
    'DESCRIPTION': 'This is just another document for testing purpose :-)',
    'sortme': '3',
}
doc3 = {
    'id_NUMBER': 7,
    'TITLE': 'thirdd',
    'DESCRIPTION': 'This is just another document for testing purpose :-)',
    'sortme': '1',
}

class TestCreateSorting(TestBase):
    mode = 'RDWR'
    dbname = 'test_sorting'
    def setUp(self):
        TestBase.setUp(self)
        ans = self.client.createdb(name=self.dbname, conf=config)
        self.client.setdb(self.dbname)

    def insert_docs(self):
        ans = self.client.insert(doc1)
        self.assertEqual(ans, {u'status': u'ok'})
        ans = self.client.insert(doc2)
        self.assertEqual(ans, {u'status': u'ok'})
        ans = self.client.insert(doc3)
        self.assertEqual(ans, {u'status': u'ok'})

    def test_query_with_sorting(self):
        self.insert_docs()
        ans = self.client.query('document')
        self.assertEqual(set(ans['results']), {1, 2, 3})
        ans = self.client.query('document', sort=[('TITLE', True)])
        self.assertEqual(ans['results'], [3, 1, 2])
        ans = self.client.query('document', sort=[('sortme', True), ('TITLE', False)])
        self.assertEqual(ans['results'], [2, 1, 3])
        ans = self.client.query('document', sort=[('sortme', True), ('TITLE', True)])
        self.assertEqual(ans['results'], [1, 2, 3])

    def tearDown(self):
        TestBase.tearDown(self)
        os.system("rm -rf '%s'" % os.path.join(dbdir, self.dbname))
        os.unlink(os.path.join(dbdir, '%s.ini' % self.dbname))

if __name__ == '__main__':
    unittest.main()

