# -*- coding: utf-8 -*-
'''
Test cases for the database model
'''
from atcatalog import app
from atcatalog.data.dbsetup import db, User, Language, Sentence, user_language
from unittest import main
from flask.ext.testing import TestCase
from tempfile import mkstemp
from functools import partial
from sqlalchemy import exc
import atcatalog.data.dbfill as dbfill
import atcatalog.data.const as const
import os


__author__ = 'Johannes Maria Frank'

class TestDBSetup(TestCase):
    '''
    Basic testing of the dbsetup module
    '''
    def create_app(self):
        '''
        Necessary for the flask testing extension module
        '''
        app.config['TESTING'] = True
        self.handle, self.dbname = mkstemp(suffix='.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = const.DB_PREFIX + self.dbname
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

    def test_insert_user(self):
        '''
        Tests if a user is inserted into the session
        '''
        user = dbfill.add_user()
        self.assertIn(user, db.session)

    def test_inserted_user(self):
        '''
        Test if the user is written into the database
        '''
        user = dbfill.add_user()
        with os.fdopen(self.handle) as dbfile:
            dbcontent = dbfile.read()
            self.assertIn(user.name.encode('ascii'), dbcontent)
            self.assertIn(user.email.encode('ascii'), dbcontent)

    def test_query_user(self):
        '''
        Test if an inserted user can be read from the database
        '''
        user = dbfill.add_user()
        query_user = User.query.filter_by(email=user.email).one()
        self.assertEqual(query_user, user)
        self.assertIn(query_user, db.session)

    def test_id_user(self):
        '''
        Tests if a user id stays with the user
        '''
        users = dbfill.add_users()
        query_users = []
        for idx in reversed(range(1,4)):
            query_users.append(User.query.filter_by(id=idx).one())
            self.assertEqual(query_users[-1].id, idx)
            self.assertEqual(query_users[-1],users[idx - 1])

    def test_serialize_user(self):
        '''
        Test the serialize function of the object
        '''
        id = 1
        name = 'Johannes'
        email = 'jmfrank63@gmail.com'
        picture = const.MALE_IMAGE
        user_dict = {'id' : id,
                     'name' : name,
                     'email' : email,
                     'picture' : picture}
        user = dbfill.add_user(User(name, email, picture))
        self.assertEqual(user.serialize, user_dict)

    def test_insert_language(self):
        '''
        Test if a language is inserted into the session
        '''
        language = dbfill.add_language()
        self.assertEqual(language.name, 'English')

    def test_inserted_language(self):
        '''
        Test if the language is written into the database
        '''
        language = dbfill.add_language()
        dbfile = open(self.dbname)
        dbcontent = dbfile.read()
        self.assertIn('English',dbcontent)

    def test_query_language(self):
        '''
        Test if an inserted language can be read from the database
        '''
        language = dbfill.add_language()
        query_language = Language.query.filter_by(name='English').one()
        self.assertEqual(query_language, language)
        self.assertIn(query_language, db.session)

    def test_id_language(self):
        '''
        Tests if a user id stays with the user
        '''
        languages = dbfill.add_languages()
        query_languages = []
        for idx in reversed(range(1,4)):
            query_languages.append(Language.query.filter_by(id=idx).one())
            self.assertEqual(query_languages[-1].id, idx)
            self.assertEqual(query_languages[-1],languages[idx - 1])

    def test_serialize_language(self):
        '''
        Test the serialize function of the language model
        '''
        id = 1
        name = 'English'
        language_dict = {'id' : id,
                         'name' : name }
        language = dbfill.add_language(Language(name))
        self.assertEqual(language.serialize, language_dict)


    def test_insert_sentence(self):
        '''
        Test if a sentence is inserted into the session
        '''
        sentence = dbfill.add_sentence()
        self.assertEqual(sentence.text, 'Hello')

    def test_inserted_sentence(self):
        '''
        Test if the sentence is written into the database
        '''
        sentence = dbfill.add_sentence()
        dbfile = open(self.dbname)
        dbcontent = dbfile.read()
        self.assertIn('file:///static/audio/hello.mp3',dbcontent)

    def test_query_sentence(self):
        '''
        Test if an inserted sentence can be read from the database
        '''
        sentence = dbfill.add_sentence()
        query_sentence = Sentence.query.filter_by(text='Hello').first()
        self.assertEqual(query_sentence, sentence)
        self.assertIn(query_sentence, db.session)

    def test_id_sentence(self):
        '''
        Tests if a user id stays with the user
        '''
        sentences = dbfill.add_sentences()
        query_sentences = []
        for idx in reversed(range(1,4)):
            query_sentences.append(Sentence.query.filter_by(id=idx).one())
            self.assertEqual(query_sentences[-1].id, idx)
            self.assertEqual(query_sentences[-1],sentences[idx - 1])

    def test_serialize_sentence(self):
        '''
        Test the serialize function of the sentence model
        '''
        id = 1
        text = 'Hello'
        translation = 'Hello'
        audio = 'file:///static/audio/hello.mp3'
        user_id = 1
        lang_id = 1
        sentence_dict = {'id' : id,
                         'text' : text,
                         'translation' : translation,
                         'audio' : audio,
                         'user_id' : user_id,
                         'lang_id' : lang_id}
        sentence = dbfill.add_sentence(Sentence(text,
                                               translation,
                                               audio,
                                               user_id,
                                               lang_id))
        self.assertEqual(sentence.serialize, sentence_dict)

    def test_add_language_to_user(self):
        '''
        Tests if languages can be added to a user
        '''
        user = dbfill.add_user()
        language = dbfill.add_language()
        self.assertFalse(user.languages)
        user.languages.append(language)
        self.assertIn(language, user.languages)

    def test_user_in_added_language(self):
        '''
        Tests if a user is in language after adding the language to the user
        '''
        user = dbfill.add_user()
        language = dbfill.add_language()
        self.assertFalse(language.users)
        user.languages.append(language)
        self.assertIn(user, language.users)

    def test_add_languages_to_users(self):
        '''
        Test if multiple languages can be added to multiple users
        '''
        users = dbfill.add_users()
        languages = dbfill.add_languages()
        for user in users:
            for language in languages:
                user.languages.append(language)
        for user in users:
            for language in languages:
                self.assertIn(language, user.languages)
        for language in user.languages:
            for user in users:
                self.assertIn(user, language.users)

class TestDBCRUD(TestCase):
    '''
    Basic testing of the dbsetup module
    '''
    def create_app(self):
        '''
        Necessary for the flask testing extension module
        '''
        app.config['TESTING'] = True
        self.handle, self.dbname = mkstemp(suffix='.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = const.DB_PREFIX + self.dbname
        return app

    def setUp(self):
        '''
        Setup the database
        '''
        db.create_all()
        self.user = dbfill.add_user()
        self.language = dbfill.add_language()
        self.sentence = dbfill.add_sentence()

    def tearDown(self):
        '''
        Drop all tables in the database so we can start again
        '''
        db.session.remove()
        db.drop_all()
        os.close(self.handle)
        os.remove(self.dbname)

    def test_create_sentence(self):
        '''
        Test if the sentence contains a valid user and language id
        '''
        self.assertEqual(self.user.id, self.sentence.user_id)
        self.assertEqual(self.language.id, self.sentence.lang_id)

    def test_unique_user(self):
        '''
        Test that email must be unique
        '''
        with self.assertRaises(exc.IntegrityError):
            dbfill.add_user()

    def test_unique_language(self):
        '''
        Test that language name is unique
        '''
        with self.assertRaises(exc.IntegrityError):
            dbfill.add_language()

    def test_unique_sentence(self):
        '''
        Test sentences are unique to a user
        '''
        with self.assertRaises(exc.IntegrityError):
            dbfill.add_sentence()

if __name__ == '__main__':
    main()
