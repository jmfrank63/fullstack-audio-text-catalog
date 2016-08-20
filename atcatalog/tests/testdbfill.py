# -*- coding: utf-8 -*-
'''
Test the dbfill module
'''
from testatcmodel import *
from atcatalog.data.const import *
from atcatalog.data.dbfill import *
from random import randint
from unittest import skipIf
from os import getenv

class TestDBFill(TestBase):
    '''
    Test the dbfill module
    '''
    @skipIf(getenv('TEST_LANGUAGE_FILL', TEST_LANGUAGE_FILL).upper() != 'TRUE',
                   "Skipping language filling test")
    def test_add_all_languages(self):
        '''
        Test the add all languages to the database
        '''
        add_all_languages()
        languages = Language.query.all()
        self.assertEqual(len(languages), len(LANG_DICT))

    @skipIf(getenv('TEST_USER_FILL', TEST_USER_FILL).upper() != 'TRUE',
                   "Skipping user filling test")
    def test_add_users(self):
        '''
        Test the adding of users to the database
        '''
        # languages have to be in there first
        add_all_languages()
        user_num = randint(1,USER_NUM)
        add_users(user_num)
        users = User.query.all()
        self.assertEqual(len(users), user_num)

    @skipIf(getenv('TEST_SENTENCE_FILL', TEST_SENTENCE_FILL) != 'TRUE',
                   "Skipping sentence filling test")
    def test_add_languages(self):
        '''
        Test the adding of languages to the database
        '''
        # languages and users have to be in there first
        add_all_languages()
        user_num = randint(1,USER_NUM)
        add_users(user_num)
        sentence_num = randint(1,SENTENCE_NUM)
        add_sentences(sentence_num)
        sentences = Sentence.query.all()
        users = User.query.all()
        user_sentence_sum = sum([len(user.sentences) for user in users])

        self.assertEqual(len(sentences), user_sentence_sum)

    @skipIf(getenv('TEST_DB_FILL', TEST_DB_FILL) != 'TRUE',
                   "Skipping database filling test")
    def test_dbfill(self):
        '''
        Test the entire filling of the database
        '''
        dbfill(USER_NUM, SENTENCE_NUM)
        languages = Language.query.all()
        users = User.query.all()
        sentences = Sentence.query.all()
        user_sentence_sum = sum([len(user.sentences) for user in users])
        self.assertEqual(len(languages), len(LANG_DICT))
        self.assertEqual(len(users), USER_NUM)
        self.assertEqual(len(sentences), user_sentence_sum)
