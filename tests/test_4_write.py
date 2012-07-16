# vim:fileencoding=utf-8:sw=4

import unittest
from base import TestBase

config = '''\
[config]
id = id_NUMBER
lang = en
indexing = TITLE, DESCRIPTION

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

class TestCreateReadOnly(TestBase):
    def test_create_with_readonly_mode(self):
        ans = self.client.createdb('test', conf=config)
        self.assertEqual(ans['status'], u'error')

class TestCreateFailure(TestBase):
    mode = 'RDWR'
    def test_bad_createdb(self):
        ans = self.client.do_cmd('createdb')
        self.assertMessageFind(ans, 'name')

    def test_createdb_noconf(self):
        ans = self.client.do_cmd('createdb', name='test')
        self.assertMessageFind(ans, 'confdata')

    def test_createdb_badconf(self):
        ans = self.client.createdb(name='test', conf=123)
        self.assertMessageFind(ans, 'invalid config')

        ans = self.client.createdb(name='test', conf=['abc', 'def'])
        self.assertMessageFind(ans, 'invalid config')

        ans = self.client.createdb(name='test', conf=dict(test='failure'))
        self.assertMessageFind(ans, 'invalid config')

if __name__ == '__main__':
    unittest.main()

