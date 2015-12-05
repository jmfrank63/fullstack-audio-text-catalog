# -*- coding: utf-8 -*-
'''
Test cases for the public languages pages
'''
from atcatalog import app
from unittest import main
from flask.ext.testing import TestCase
from random import randint
from atcatalog.data.fake import LANGUAGES, SENTENCES

__author__ = 'Johannes Maria Frank'


class TestLanguages(TestCase):
    '''
    Basic testing of the language site
    '''
    def create_app(self):
        '''
        Necessary for the flask testing extension module
        '''
        app.config['TESTING'] = True
        return app

    def setUp(self):
        '''
        Setup the database
        '''
        pass

    def tearDown(self):
        '''
        Drop all tables in the database so we can start again
        '''
        pass

    def test_status_codes(self):
        '''
        Test the return status code of public language.
        '''
        self.assert200(self.client.get('/'))

    def test_page_loads(self):
        '''
        Test that the public language site actually loads.
        '''
        self.client.get('/')
        self.assert_template_used('show_languages.html')

    def test_languages_show(self):
        '''
        Test that language actually show up on page
        '''
        response = self.client.get('/')
        for id, language in LANGUAGES.iteritems():
            self.assertIn(language.capitalize(), response.data)



if __name__ == '__main__':
    main()
