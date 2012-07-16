# vim:fileencoding=utf-8:sw=4

import unittest
from base import TestBase

q1 = {u'status': u'ok', u'results': [3361, 29527, 179280, 108983, 5347, 39799, 88628, 142556, 182570, 141853, 141106, 178864, 102161, 144520, 167934, 70001, 22417, 104604, 87553, 123069]}

q2 = {u'status': u'ok', u'results': [3361, 29527, 108983, 5347, 39799, 182570, 70001, 4172, 4203, 5090, 5312, 6110, 6383, 6520, 6808, 6837, 8971, 25098, 25558, 26534]}

class TestQuery(TestBase):
    def setUp(self):
        super(TestQuery, self).setUp()
        self.client.set(name='indexdb', value='db')

    def test_simpleQuery(self):
        ans = self.client.query('water')
        self.assertEqual(ans, q1)

    def test_titleQuery(self):
        ans = self.client.query('title:water')
        self.assertEqual(ans, q2)

if __name__ == '__main__':
    unittest.main()
