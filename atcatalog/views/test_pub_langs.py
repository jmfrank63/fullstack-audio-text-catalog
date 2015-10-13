'''
Test cases for the public languages pages
'''
from unittest import TestCase, main
from atcatalog import app
from random import randint

__author__ = 'johannesfrank'


class TestPub_langs(TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_status_code(self):
        '''
        Test the return status code.
        '''
        response = self.test_client.get('/langs/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_page_loads(self):
        '''
        Test that the page actually loads
        '''
        response = self.test_client.get('/langs/', content_type='html/text')
        self.assertIn('<title>Public Languages</title>', response.data)


class TestPub_lang(TestCase):
    def test_status_code(self):
        '''
        Test the return status code
        '''
        test_client = app.test_client(self)
        lid = randint(1, 100)
        response = test_client.get('/lang/{0}/'.format(lid),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    main()
