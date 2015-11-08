'''
Test cases for the public sentences pages
'''
from flask import Flask
from flask.ext.testing import TestCase
from random import randint
from atcatalog.langdata.langdicts import language

__author__ = 'Johannes Maria Frank'


class TestPubSents(TestCase):
    '''
    Test the public languages list
    '''
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        app = self.create_app()
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
    '''
    Test the public language content_type
    '''
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        app = self.create_app()
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
    unittest.main()
