# vim:fileencoding=utf-8:sw=4

import os
import unittest
from base import TestBase, dbdir

config = '''\
[config]
id = id
lang = zh
indexing = TITLE, DESCRIPTION, extra

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

doc1 = {
    'id': "abc",
    'TITLE': '中文测试',
    'DESCRIPTION': '让我们来测试下中文的支持。将被索引的 Testing 文档!',
}

doc2 = {
    'id': "def",
    'TITLE': '文本应该是按词索引的',
    'DESCRIPTION': '所以查询“文”应当只返回此文档！',
}

class TestZh(TestBase):
    mode = 'RDWR'
    dbname = 'test_zh'
    def setUp(self):
        super(TestZh, self).setUp()
        ans = self.client.createdb(name=self.dbname, conf=config)
        self.client.setdb(self.dbname)

    def insert_docs(self):
        ans = self.client.insert(doc1)
        self.assertEqual(ans, {u'status': u'ok'})
        ans = self.client.insert(doc2)
        self.assertEqual(ans, {u'status': u'ok'})

    def test_query(self):
        self.insert_docs()
        ans = self.client.query('中文')
        self.assertEqual(ans['results'], [1])
        ans = self.client.query('文')
        self.assertEqual(ans['results'], [2])
        ans = self.client.query('title:索引')
        self.assertEqual(ans['results'], [2])
        ans = self.client.query('test')
        self.assertEqual(ans['results'], [1])
        ans = self.client.query('tested')
        self.assertEqual(ans['results'], [1])
        ans = self.client.query('title:文本索引')
        self.assertEqual(ans['results'], [2])
        ans = self.client.query('test文档')
        self.assertEqual(ans['results'], [1])

    def tearDown(self):
        super(TestZh, self).tearDown()
        os.system("rm -rf '%s'" % os.path.join(dbdir, self.dbname))
        os.unlink(os.path.join(dbdir, '%s.ini' % self.dbname))

if __name__ == '__main__':
    unittest.main()

