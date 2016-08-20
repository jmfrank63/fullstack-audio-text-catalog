# -*- coding: utf-8 -*-
'''
Test cases for the database model
'''
from atcatalog import app
from atcatalog.model.atcmodel import *
from flask.ext.sqlalchemy import SQLAlchemy, SignallingSession
from atcatalog.data.gendata import *
from unittest import main
from flask.ext.testing import TestCase
from tempfile import mkstemp
from functools import partial
from sqlalchemy import exc, and_
from atcatalog.data.const import *
from random import randint
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
    Test the language class
    '''
    @classmethod
    def setUpClass(self):
        '''
        create a random language code and use it for all tests
        '''
        self.code = create_random_code()

    def setUp(self):
        '''
        Add the language to the session and commit
        '''
        super(TestLanguage, self).setUp()
        self.language = Language(self.code)
        db.session.add(self.language)
        db.session.commit()

    def test_insert_language(self):
        '''
        Test if a language can be inserted into the session
        '''
        self.assertIn(self.language, db.session)

    def test_query_language(self):
        '''
        Test if an inserted language can be read from the database
        '''
        query_language = Language.query.filter_by(code=self.language.code).one()
        self.assertEqual(query_language, self.language)

    def test_id_language(self):
        '''
        Tests if a user id stays with the user
        '''
        self.assertEqual(Language.query.get(1).id, self.language.id)

    def test_repr_language(self):
        '''
        Test the repr of the object
        '''
        self.assertEqual(self.language.__repr__(),
                         "<Language(id=1, code='{0}')>".format(self.code))

    def test_serialize_language(self):
        '''
        Test the serialize function of the language model
        '''
        language_dict = {'id' : self.language.id,
                         'code' : self.language.code }
        self.assertEqual(self.language.serialize, language_dict)


class TestUser(TestBase):
    '''
    Test the user class
    '''
    def setUp(self):
        '''
        Add all languages to the database at the beginning of each test
        create codes to use,
        create a user and add him to the database
        '''
        super(TestUser, self).setUp()
        db.session.add_all([Language(code) for code in create_all_codes()])
        db.session.commit()
        self.codes = create_random_codes(LANG_NUM)
        self.user = User(*create_random_user_data(self.codes))
        db.session.add(self.user)
        db.session.commit()

    def test_insert_user(self):
        '''
        Tests if a user can be inserted into the session
        '''
        self.assertIn(self.user, db.session)

    def test_query_user(self):
        '''
        Test if an inserted user can be read from the database
        '''
        user = User.query.filter_by(email=self.user.email).one()
        self.assertEqual(user, self.user)

    def test_id_user(self):
        '''
        Tests if a user id is created and if it is 1
        '''
        user = User.query.get(1)
        self.assertEqual(user.id, 1)

    def test_repr_user(self):
        '''
        Test the repr of the object
        '''
        user = User.query.get(1)
        self.assertEqual(user.__repr__(),
                         u"<User(id=1, name='{}', \
email='{}', \
codes='{}', \
picture='{}', \
languages='{}', \
sentences='{}')>".format(user.name,
                          user.email,
                          user.codes,
                          user.picture,
                          user.languages,
                          user.sentences,
                         ).encode('utf-8'))


    def test_serialize_user(self):
        '''
        Test the serialize function of the object
        '''
        user = User.query.get(1)
        user_dict = {'id' : self.user.id,
                     'name' : self.user.name,
                     'email' : self.user.email,
                     'codes' : self.user.codes,
                     'picture' : self.user.picture,
                     'languages' : self.user.languages,
                     'sentences' : self.user.sentences}
        self.assertEqual(user.serialize, user_dict)


class TestSentence(TestBase):
    '''
    Test the sentence class
    '''
    def setUp(self):
        '''
        Add all languages to the database at the beginning of each test
        create codes to use,
        create two users and add them to the database,
        create a sentence and add it to the database
        '''
        super(TestSentence, self).setUp()
        db.session.add_all([Language(code) for code in create_all_codes()])
        db.session.commit()
        self.codes = create_random_codes(LANG_NUM)
        self.user = User(*create_random_user_data(self.codes))
        db.session.add(self.user)
        self.second_user = User(*create_random_user_data(self.codes))
        db.session.add(self.second_user)
        db.session.commit()
        self.language = Language.query.get(randint(1, LANG_NUM))
        self.sentence = Sentence(*create_random_sentence_data(self.language.id,
                                                              self.user.id
                                                             ))
        db.session.add(self.sentence)
        db.session.commit()


    def test_insert_sentence(self):
        '''
        Test if a sentence is inserted into the session
        '''
        self.assertIn(self.sentence, db.session)

    def test_query_sentence(self):
        '''
        Test if an inserted sentence can be read from the database
        '''
        sentence = Sentence.query.filter_by(text=self.sentence.text).first()
        query_sentence = Sentence.query.filter(
             and_(Sentence.text == self.sentence.text,
                  Sentence.language_id == self.sentence.language_id)
                 ).one()
        self.assertEqual(query_sentence, self.sentence)

    def test_id_sentence(self):
        '''
        Tests if a user id stays with the user
        '''
        language = Language.query.get(1)
        self.assertEqual(language.id, 1)

    def test_repr_sentence(self):
        '''
        Test the repr of the object
        '''
        sentence = Sentence.query.get(1)
        self.assertEqual(sentence.__repr__(),
                         u"<Sentence(id={}, text='{}', translation='{}', \
audio='{}', language_id='{}', user_id='{}')>".format(sentence.id,
                                                        sentence.text,
                                                        sentence.translation,
                                                        sentence.audio,
                                                        sentence.language_id,
                                                        sentence.user_id,
                                                       ).encode('utf-8'))

    def test_serialize_sentence(self):
        '''
        Test the serialize function of the sentence model
        '''
        sentence = Sentence.query.get(1)
        sentence_dict = {'id' : self.sentence.id,
                         'text' : self.sentence.text,
                         'translation' : self.sentence.translation,
                         'audio' : self.sentence.audio,
                         'user_id' : self.sentence.user_id,
                         'language_id' : self.sentence.language_id}
        self.assertEqual(sentence.serialize, sentence_dict)

class TestATCModel(TestBase):
    '''
    Test the removal and recreation of the database
    '''
    def test_remove_database(self):
        '''
        Test the database file is deleted
        '''
        handle, dbname = mkstemp(suffix='.db')
        remove_database(dbname)
        self.assertFalse(os.path.exists(dbname))

    def test_atcmodel_new(self):
        '''
        Test if database is created when it doesn't exist
        '''
        atcmodel(True)
        self.assertTrue(isSQLite3(self.dbname))

    def test_atcmodel_exists(self):
        '''
        Test if the database is reused if it already exists
        '''
        db.create_all()
        existing_dbname = self.dbname
        atcmodel()
        self.assertTrue(isSQLite3(existing_dbname))
        self.assertEqual(existing_dbname, self.dbname)

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
