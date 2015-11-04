'''
Test cases for the public languages pages
'''
from unittest import TestCase, main
from atcatalog import app
from random import randint
from atcatalog.langdata.langdicts import language

__author__ = 'johannesfrank'


class TestPubLangs(TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_status_code(self):
        '''
        Test the return status code of public language.
        '''
        response = self.test_client.get('/langs/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_page_loads(self):
        '''
        Test that the public language site actually loads.
        '''
        response = self.test_client.get('/langs/', content_type='html/text')
        self.assertIn('<title>Public Languages</title>', response.data)

    def test_languages_show(self):
        '''
        Test that language actually show up on page
        '''


class TestPubLang(TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_status_code(self):
        '''
        Test the return status code
        '''
        lid = randint(1, 100)
        response = self.test_client.get('/lang/{0}/'.format(lid),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    main()
