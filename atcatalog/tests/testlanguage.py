# -*- coding: utf-8 -*-
'''
Test cases for the public language pages
'''
from atcatalog import app
from unittest import main
from flask.ext.testing import TestCase
from flask import Flask
from random import randint
from atcatalog.data.fake import LANGUAGES, SENTENCES
from random import randint

__author__ = 'Johannes Maria Frank'


class TestLanguage(TestCase):
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
        self.lid = randint(0, 4)

    def tearDown(self):
        '''
        Drop all tables in the database so we can start again
        '''
        pass

    def test_status_codes(self):
        '''
        Test the return status code of public language.
        '''
        self.assert200(self.client.get('/language/{0}/'.format(self.lid)))

    def test_page_loads(self):
        '''
        Test that the public language site actually loads.
        '''
        self.client.get('/language/{0}/'.format(self.lid))
        self.assert_template_used('show_language.html')

    def test_sentences_show(self):
        '''
        Test that language actually show up on page
        '''
        response = self.client.get('/language/{0}/'.format(self.lid))
        for id, sentence in SENTENCES[self.lid].iteritems():
            self.assertIn(sentence[1], response.data.decode('utf-8'))


if __name__ == '__main__':
    main()
