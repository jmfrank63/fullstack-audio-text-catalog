# -*- coding: utf-8 -*-
'''
Test cases for the database model
'''
from atcatalog import app
from atcatalog.model.atcmodel import db, User, Language, Sentence, user_language
from flask.ext.sqlalchemy import SQLAlchemy, SignallingSession
from atcatalog.data.gendata import create_random_code, \
                                   create_random_codes, \
                                   create_random_user_data
from unittest import main
from flask.ext.testing import TestCase
from tempfile import mkstemp
from functools import partial
from sqlalchemy import exc
from atcatalog.data.dbfill import add_all_languages
from atcatalog.data.const import *
import os


__author__ = 'Johannes Maria Frank'

class TestBase(TestCase):
    '''
    Base test class and common setup
    '''
    def create_app(self):
        '''
        Necessary for the flask testing extension module
        '''
        app.config['TESTING'] = True
        self.handle, self.dbname = mkstemp(suffix='.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = DB_PREFIX + self.dbname
        return app

    def setUp(self):
        '''
        Setup the database
        '''
        db.create_all()

    def tearDown(self):
        '''
        Drop all tables in the database so we can start again
        '''
        db.session.remove()
        db.drop_all()
        os.remove(self.dbname)


class TestLanguage(TestBase):
    '''
    Basic inserting testing of the dbsetup module
    '''
    def test_insert_language(self):
        '''
        Test if a language can be inserted into the session
        '''
        code = create_random_code()
        language = Language(code)
        db.session.add(language)
        db.session.commit()
        self.assertIn(language, db.session)

    def test_query_language(self):
        '''
        Test if an inserted language can be read from the database
        '''
        language = Language(create_random_code())
        db.session.add(language)
        db.session.commit()
        query_language = Language.query.filter_by(code=language.code).one()
        self.assertEqual(query_language, language)

    def test_id_language(self):
        '''
        Tests if a user id stays with the user
        '''
        language = Language(create_random_code())
        db.session.add(language)
        db.session.commit()
        self.assertEqual(Language.query.get(1).id, language.id)

    def test_serialize_language(self):
        '''
        Test the serialize function of the language model
        '''
        language = Language(create_random_code())
        db.session.add(language)
        db.session.commit()
        db.session.add(language)
        language_dict = {'id' : language.id,
                         'code' : language.code }
        self.assertEqual(language.serialize, language_dict)


class TestUser(TestBase):
    '''
    Test the user classs
    '''
    def setUp(self):
        '''
        User testing specific setup
        '''
        super(TestUser, self).setUp()
        # We must make sure languages are already in the database
        add_all_languages()

    def test_insert_user(self):
        '''
        Tests if a user can be inserted into the session
        '''
        codes = create_random_codes(LANG_NUM)
        user = User(*create_random_user_data(codes))
        db.session.add(user)
        self.assertIn(user, db.session)

    def test_query_user(self):
        '''
        Test if an inserted user can be read from the database
        '''
        codes = create_random_codes(LANG_NUM)
        user = User(*create_random_user_data(codes))
        db.session.add(user)
        db.session.commit()
        db.session.add(user)
        query_user = User.query.filter_by(email=user.email).one()
        self.assertEqual(query_user, user)

    def test_id_user(self):
        '''
        Tests if a user id is created
        '''
        code = create_random_code()
        user = User(*create_random_user_data([code]))
        db.session.add(user)
        db.session.commit()
        user = User.query.get(1)
        self.assertEqual(user.id, 1)

    # def test_serialize_user(self):
    #     '''
    #     Test the serialize function of the object
    #     '''
    #     codes = create_random_codes(5)
    #     languages = [Language(code) for code in codes]
    #     db.session.add_all(languages)
    #     db.session.commit()
    #     db.session.add_all(languages)
    #     user = create_random_user(codes)
    #     db.session.add(user)
    #     db.session.commit()
    #     db.session.add_all(languages)
    #     db.session.add(user)
    #     sentences = [create_random_sentence(language, user)
    #                  for language in languages
    #                  for _ in xrange(5)]
    #     db.session.add_all(sentences)
    #     db.session.commit()
    #     user_dict = {'id' : user.id,
    #                  'name' : user.name,
    #                  'email' : user.email,
    #                  'codes' : codes,
    #                  'picture' : user.picture,
    #                  'languages' : languages,
    #                  'sentences' : sentences}
    #     self.assertEqual(user.serialize, user_dict)

#     def test_insert_sentence(self):
#         '''
#         Test if a sentence is inserted into the session
#         '''
#         dbfill.add_language()
#         dbfill.add_user()
#         sentence = dbfill.add_sentence()
#         self.assertEqual(sentence.text, 'Hello')

#     def test_query_sentence(self):
#         '''
#         Test if an inserted sentence can be read from the database
#         '''
#         dbfill.add_language()
#         dbfill.add_user()
#         sentence = dbfill.add_sentence()
#         query_sentence = Sentence.query.filter_by(text='Hello').first()
#         self.assertEqual(query_sentence, sentence)
#         self.assertIn(query_sentence, db.session)

#     def test_id_sentence(self):
#         '''
#         Tests if a user id stays with the user
#         '''
#         languages = dbfill.add_languages()
#         user = dbfill.add_user()
#         sentences = dbfill.add_sentences()
#         query_sentences = []
#         for idx in reversed(range(1,4)):
#             query_sentences.append(Sentence.query.filter_by(id=idx).one())
#             self.assertEqual(query_sentences[-1].id, idx)
#             self.assertEqual(query_sentences[-1],sentences[idx - 1])

#     def test_serialize_sentence(self):
#         '''
#         Test the serialize function of the sentence model
#         '''
#         id = 1
#         text = 'Hello'
#         translation = 'Hello'
#         audio = 'file:///static/audio/hello.mp3'
#         user_id = 1
#         lang_id = 1
#         sentence_dict = {'id' : id,
#                          'text' : text,
#                          'translation' : translation,
#                          'audio' : audio,
#                          'user_id' : user_id,
#                          'lang_id' : lang_id}
#         dbfill.add_language()
#         dbfill.add_user()
#         sentence = dbfill.add_sentence(Sentence(text,
#                                               translation,
#                                               audio,
#                                               user_id,
#                                               lang_id))
#         self.assertEqual(sentence.serialize, sentence_dict)

#     def test_add_language_to_user(self):
#         '''
#         Tests if languages can be added to a user
#         '''
#         language = dbfill.add_language()
#         user = dbfill.add_user()
#         self.assertFalse(user.languages)
#         user.languages.append(language)
#         self.assertIn(language, user.languages)

#     def test_user_in_added_language(self):
#         '''
#         Tests if a user is in language after adding the language to the user
#         '''
#         language = dbfill.add_language()
#         user = dbfill.add_user()
#         self.assertFalse(language.users)
#         user.languages.append(language)
#         self.assertIn(user, language.users)

#     def test_add_languages_to_users(self):
#         '''
#         Test if multiple languages can be added to multiple users
#         '''
#         languages = dbfill.add_languages()
#         users = dbfill.add_users()
#         for user in users:
#             for language in languages:
#                 user.languages.append(language)
#         for user in users:
#             for language in languages:
#                 self.assertIn(language, user.languages)
#         for language in user.languages:
#             for user in users:
#                 self.assertIn(user, language.users)

# class TestDBConstraints(TestCase):
#     '''
#     Basic constraints testing of the dbsetup module
#     '''
#     def create_app(self):
#         '''
#         Necessary for the flask testing extension module
#         '''
#         app.config['TESTING'] = True
#         self.handle, self.dbname = mkstemp(suffix='.db')
#         app.config['SQLALCHEMY_DATABASE_URI'] = DB_PREFIX + self.dbname
#         return app

#     def setUp(self):
#         '''
#         Setup the database
#         '''
#         db.create_all()
#         self.language = dbfill.add_language()
#         self.user = dbfill.add_user()
#         self.sentence = dbfill.add_sentence()

#     def tearDown(self):
#         '''
#         Drop all tables in the database so we can start again
#         '''
#         db.session.remove()
#         db.drop_all()
#         os.close(self.handle)
#         os.remove(self.dbname)

#     def test_create_valid_sentence(self):
#         '''
#         Test if the sentence contains a valid user and language id
#         '''
#         self.assertEqual(self.user.id, self.sentence.user_id)
#         self.assertEqual(self.language.id, self.sentence.lang_id)

#     def test_fail_unique_user(self):
#         '''
#         Test that email must be unique
#         '''
#         with self.assertRaises(exc.IntegrityError):
#             dbfill.add_user()

#     def test_fail_unique_language(self):
#         '''
#         Test that language name is unique
#         '''
#         with self.assertRaises(exc.IntegrityError):
#             dbfill.add_language()

#     def test_fail_unique_sentence(self):
#         '''
#         Test sentences are unique to a user
#         '''
#         with self.assertRaises(exc.IntegrityError):
#             dbfill.add_sentence()

#     def test_fail_sentence_nonexistent_user(self):
#         '''
#         Tests adding a sentence without existing user id
#         '''
#         sentence = Sentence('Hallo', 'Hello', AUDIO_DUMMY, 42, 1)
#         with self.assertRaises(exc.IntegrityError):
#             dbfill.add_sentence(sentence)

#     def test_fail_sentence_nonexistent_language(self):
#         '''
#         Tests adding a sentence without existing language id
#         '''
#         sentence = Sentence('Hallo', 'Hello', AUDIO_DUMMY, 1, 42)
#         with self.assertRaises(exc.IntegrityError):
#             dbfill.add_sentence(sentence)

#     def test_fail_user_nonexistent_language(self):
#         '''
#         Test add a user without existing language id
#         '''
#         user = User('John Doe', 'johndoe@example.com', MALE_IMAGE, 42)
#         with self.assertRaises(exc.IntegrityError):
#             dbfill.add_user(user)

if __name__ == '__main__':
    main()
