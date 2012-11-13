# vim:fileencoding=utf-8:sw=4

import os
import unittest
from base import TestBase, dbdir, config

bad_config1 = '''\
[config]
version = 1.1
lang = en
indexing = TITLE, DESCRIPTION, extra

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

bad_config2 = '''\
[config]
version = 1.1
id = id_NUMBER
lang = en
indexing = DESCRIPTION, extra

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

bad_config3 = '''\
[config]
version = 1.1
id = id_NUMBER
lang = en
indexing = TITLE, DESCRIPTION, extra

[field_prefix]
S = TITLE
XD = DESCRIPTION
EX = extra

[prefix_name]
S = title
XD = description
'''

bad_config4 = '''gabage here :-)'''

bad_config5 = '''\
[config]
version = 1.1
id = id_NUMBER
lang = wtf
indexing = TITLE, DESCRIPTION, extra

[field_prefix]
S = TITLE
XD = DESCRIPTION

[prefix_name]
S = title
XD = description
'''

bad_config6 = '''\
[config]
version = 1.1
id = id_NUMBER
lang = en
indexing = TITLE, DESCRIPTION, extra

[field_prefix]
S = TITLE
XD = DESCRIPTION
Q = extra

[prefix_name]
S = title
XD = description
Q = extra
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

        ans = self.client.createdb(name='test', conf=bad_config1)
        self.assertMessageFind(ans, 'invalid config')
        ans = self.client.createdb(name='test', conf=bad_config2)
        self.assertMessageFind(ans, 'invalid config')
        ans = self.client.createdb(name='test', conf=bad_config3)
        self.assertMessageFind(ans, 'invalid config')
        ans = self.client.createdb(name='test', conf=bad_config4)
        self.assertMessageFind(ans, 'invalid config')
        ans = self.client.createdb(name='test', conf=bad_config5)
        self.assertMessageFind(ans, 'unspported lang')
        ans = self.client.createdb(name='test', conf=bad_config6)
        self.assertMessageFind(ans, 'reserved')

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
        TestBase.tearDown(self)
        os.system("rm -rf '%s'" % os.path.join(dbdir, self.dbname))
        os.unlink(os.path.join(dbdir, '%s.ini' % self.dbname))

if __name__ == '__main__':
    unittest.main()

