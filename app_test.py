"""Testing App Flask with Unittest and Pytest"""

import unittest
from app import app


class appTest(unittest.TestCase):
    '''
    Test APP
    to run use: python -m unittest app_test.py
    or
    to run use: python -m pytest
    '''

    def setUp(self):
        self.app = app.test_client()

    def test_get_8_recommendations_succeeds(self):
        rv = self.app.get('''/rec/8/sativa,energetic,
                            talkative,euphoric,creative,
                            focused,spicy,tangy,sweet''')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'''[696,942,1228,1335,
                                       1953,2120,1761,523]''')

    def test_get_5_recommendations_succeeds(self):
        rv = self.app.get('''/rec/5/hybrid,euphoric,
                            energetic,creative,woody,earthy''')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'''[736,1585,873,2310,23]''')

    def test_get_5_recommendations_without_filters_404(self):
        rv = self.app.get('''/rec/5''')
        self.assertEqual(rv.status, '404 NOT FOUND')

    def test_get_recommendations_without_result_count_404(self):
        rv = self.app.get('''/rec''')
        self.assertEqual(rv.status, '404 NOT FOUND')

    def test_get_strains_succeeds(self):
        rv = self.app.get("/strains")
        assert rv.status == '200 OK'
        assert b'hybrid' in rv.data
        assert b'100-Og' in rv.data
        assert b'Earthy,Sweet,Citrus' in rv.data

    def test_404(self):
        rv = self.app.get('/strainz')
        self.assertEqual(rv.status, '404 NOT FOUND')


if __name__ == '__main__':
    unittest.main()
