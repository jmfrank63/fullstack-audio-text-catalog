# -*- coding: utf-8 -*-
'''
Test cases for the public languages pages
'''
from atcatalog import app
from unittest import main
from flask.ext.testing import TestCase
from random import randint
from atcatalog.model.atcmodel import *
from atcatalog.tests.testatcmodel import TestBase
from atcatalog.data.dbfill import *

__author__ = 'Johannes Maria Frank'


class TestLanguages(TestBase):
    '''
    Basic testing of the language site
    '''
    def setUp(self):
        '''
        Add all languages the database
        '''
        super(TestLanguages, self).setUp()
        add_all_languages()

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

    def test_show_languages(self):
        '''
        Test that language actually show up on page
        '''
        response = self.client.get('/')
        languages = Language.query.all()
        self.assertIsNotNone(languages)
        for language in languages:
            self.assertIn(language.name, response.data)



if __name__ == '__main__':
    main()
