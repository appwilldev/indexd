# vim:fileencoding=utf-8:sw=4

import unittest
from base import TestBase

q1 = {u'status': u'ok', u'results': [3361, 29527, 179280, 108983, 5347, 39799, 88628, 142556, 182570, 141853, 141106, 178864, 102161, 144520, 167934, 70001, 22417, 104604, 87553, 123069]}

q2 = {u'status': u'ok', u'results': [3361, 29527, 108983, 5347, 39799, 182570, 70001, 4172, 4203, 5090, 5312, 6110, 6383, 6520, 6808, 6837, 8971, 25098, 25558, 26534]}

doc123 = {u'MEASUREMENTS': u'overall: 235 mm 115 mm,', u'DESCRIPTION': u'Model by Dent showing the mechanism of stop watches (full size)', u'PLACE_MADE': '', u'id_NUMBER': u'1883-69', u'WHOLE_PART': u'WHOLE', u'TITLE': u'Model by Dent showing the mechanism of stop watches (full si', u'DATE_MADE': '', u'COLLECTION': u'SCM - Time Measurement', u'ITEM_NAME': u'model - representation; stop-watch', u'MATERIALS': '', u'MAKER': u'E. Dent & Co.'}

doc1000 = {u'MEASUREMENTS': '', u'DESCRIPTION': u'White light reflection hologram of a necklace, made by Holofax Ltd. in 1986, using the " Holocam 50" camera', u'PLACE_MADE': '', u'id_NUMBER': u'1986-644', u'WHOLE_PART': u'WHOLE', u'TITLE': u'White light reflection hologram of a necklace, made by Holof', u'DATE_MADE': '', u'COLLECTION': u'SCM - Optics', u'ITEM_NAME': '', u'MATERIALS': '', u'MAKER': u'Holofax Limited'}

class TestQuery(TestBase):
    def setUp(self):
        super(TestQuery, self).setUp()
        self.client.setdb('db')

    def test_simpleQuery(self):
        ans = self.client.query('water')
        self.assertEqual(ans, q1)

    def test_titleQuery(self):
        ans = self.client.query('title:water')
        self.assertEqual(ans, q2)

    def test_retrieve(self):
        ans = self.client.retrieve([123, 0, -34, 1000, "abc"])
        self.assertEqual(ans, {
            u'status': u'ok',
            u'results': [doc123, None, None, doc1000, None],
        })

class TestNoDBSelected(TestBase):
    def test_simpleQuery(self):
        ans = self.client.query('water')
        self.assertMessageFind(ans, 'set indexdb first')

    def test_retrieve(self):
        ans = self.client.retrieve([123, 0, -34, 1000, "abc"])
        self.assertMessageFind(ans, 'set indexdb first')

if __name__ == '__main__':
    unittest.main()
