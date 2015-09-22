from unittest import TestCase
from atcatalog import app

__author__ = 'johannesfrank'


class TestShow_pub_langs(TestCase):
    def test_show_pub_langs_statuscode(self):
        '''
        Test the return status code.
        '''
        test_client = app.test_client(self)
        response = test_client.get('/langs/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
