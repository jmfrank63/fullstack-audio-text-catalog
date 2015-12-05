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
    Basic testing of the sentence site
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
        self.sid = randint(0, 1)

    def tearDown(self):
        '''
        Drop all tables in the database so we can start again
        '''
        pass

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
        text = SENTENCES[self.lid][self.sid][1]
        self.assertIn(text, response.data.decode('utf-8'))


    def test_sentence_translation(self):
        '''
        Test that the text actually shows up on page
        '''
        response = self.client.get('/language/{0}/sentence/{1}/'
                                   .format(self.lid, self.sid))
        translation = SENTENCES[self.lid][self.sid][2]
        self.assertIn(translation, response.data.decode('utf-8'))


    def test_sentence_audio(self):
        '''
        Test that the text actually shows up on page
        '''
        response = self.client.get('/language/{0}/sentence/{1}/audio/'
                                   .format(self.lid, self.sid))
        audio = SENTENCES[self.lid][self.sid][3]
        self.assertIn(audio, response.data.decode('utf-8'))


if __name__ == '__main__':
    main()
