# -*- coding: utf-8 -*-
'''
Test cases for the public language pages
'''
from atcatalog import app
from unittest import main
from flask.ext.testing import TestCase

from random import randint
from atcatalog.model.atcmodel import *
from atcatalog.data.const import LANG_DICT
from random import randint
from atcatalog.tests.testatcmodel import TestBase
from atcatalog.data.dbfill import *

__author__ = 'Johannes Maria Frank'


class TestLanguage(TestBase):
    '''
    Basic testing of the language site
    '''
    def setUp(self):
        '''
        Add all languages to the database
        '''
        super(TestLanguage, self).setUp()
        add_all_languages()
        self.lid = randint(1, len(LANG_DICT))
        add_users(3)
        add_sentences(3)

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
        Test that sentences actually show up on page
        '''
        response = self.client.get('/language/{0}/'.format(self.lid))
        sentences = Sentence.query.filter_by(language_id=self.lid)
        for sentence in sentences: # pragma no branch
            self.assertIn(sentence.text, response.data.decode('utf-8'))

    def test_no_sentences_(self):
        '''
        Test that no sentences are displayed properly
        '''
        self.fail('No sentences not yet implemented')

if __name__ == '__main__':
    main()
