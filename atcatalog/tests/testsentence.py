# -*- coding: utf-8 -*-
'''
Test cases for the public languages pages
'''
from atcatalog import app
from unittest import main
from flask.ext.testing import TestCase
from random import randint
from sqlalchemy import and_
from atcatalog.model.atcmodel import *
from atcatalog.data.const import LANG_DICT
from random import randint
from atcatalog.tests.testatcmodel import TestBase
from atcatalog.data.dbfill import *

__author__ = 'Johannes Maria Frank'


class TestSentence(TestBase):
    '''
    Basic testing of the sentence site
    '''
    def setUp(self):
        '''
        Add all languages to the database

        '''
        super(TestSentence, self).setUp()
        add_all_languages()
        add_users(2)
        add_sentences(2)
        sentence = Sentence.query.filter_by(user_id=randint(1,2)).first()
        self.lid = sentence.language_id
        self.sid = sentence.id

    def test_status_codes(self):
        '''
        Test the return status code of public language.
        '''
        self.assert200(self.client.get('language/{0}/sentence/{1}/'
                                       .format(self.lid, self.sid)))

    def test_page_loads(self):
        '''
        Test that the public language site actually loads.
        '''
        self.client.get('language/{0}/sentence/{1}/'
                        .format(self.lid, self.sid))
        self.assert_template_used('show_sentence.html')

    def test_sentence_show_text(self):
        '''
        Test that the public language site actually loads.
        '''
        self.client.get('language/{0}/sentence/{1}/text/'
                        .format(self.lid, self.sid))
        self.assert_template_used('show_sentence_text.html')


    def test_sentence_show_translation(self):
        '''
        Test that the public language site actually loads.
        '''
        self.client.get('language/{0}/sentence/{1}/translation/'
                        .format(self.lid, self.sid))
        self.assert_template_used('show_sentence_translation.html')

    def test_sentence_show_audio(self):
        '''
        Test that the public language site actually loads.
        '''
        self.client.get('language/{0}/sentence/{1}/audio/'
                        .format(self.lid, self.sid))
        self.assert_template_used('show_sentence_audio.html')



    def test_sentence_text(self):
        '''
        Test that the text actually shows up on page
        '''
        response = self.client.get('/language/{0}/sentence/{1}/'
                                  .format(self.lid, self.sid))
        sentence = Sentence.query.filter(and_(Sentence.language_id == self.lid,
                                              Sentence.id == self.sid)).first()
        self.assertIn(sentence.text, response.data.decode('utf-8'))


    def test_sentence_translation(self):
        '''
        Test that the text actually shows up on page
        '''
        response = self.client.get('/language/{0}/sentence/{1}/'
                                  .format(self.lid, self.sid))
        sentence = Sentence.query.filter(and_(Sentence.language_id == self.lid,
                                              Sentence.id == self.sid)).first()
        self.assertIn(sentence.translation, response.data.decode('utf-8'))


    def test_sentence_audio(self):
        '''
        Test that the text actually shows up on page
        '''
        response = self.client.get('/language/{0}/sentence/{1}/audio/'
                                  .format(self.lid, self.sid))
        sentence = Sentence.query.filter(and_(Sentence.language_id == self.lid,
                                              Sentence.id == self.sid)).first()
        self.assertIn(sentence.audio, response.data.decode('utf-8'))


if __name__ == '__main__':
    main()
