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
import os

__author__ = 'Johannes Maria Frank'

DB_PREFIX = 'sqlite:///'
MALE_IMAGE = 'file:///static/images/male.png'
FEMALE_IMAGE = 'file:///static/images/female.png'
AUDIO_DUMMY = 'file:///static/audio/dummy.mp3'

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
        try:
            os.close(self.handle)
        except OSError:
            pass
        os.remove(self.dbname)

    def _add_user(self, user=None):
        '''
        Helper function inserting a default user into the database
        '''
        if user is None:
            user = User('Johannes', 'jmfrank63@gmail.com',
                        MALE_IMAGE)
        db.session.add(user)
        db.session.commit()
        return user

    def _add_users(self):
        '''
        Adds several users to the database
        '''
        users = []
        users.append(self._add_user(User('Ted',
                                         'ted@example.com',
                                         MALE_IMAGE)))
        users.append(self._add_user(User('Jane',
                                         'janedoe@example.com',
                                         FEMALE_IMAGE)))
        users.append(self._add_user(User('John',
                                         'johndoe@example.com',
                                         MALE_IMAGE)))
        users.append(self._add_user(User('Sarah',
                                         'sarah@example.com',
                                         FEMALE_IMAGE)))
        return users

    def test_insert_user(self):
        '''
        Tests if a user is inserted into the session
        '''
        user = self._add_user()
        self.assertIn(user, db.session)

    def test_inserted_user(self):
        '''
        Test if the user is written into the database
        '''
        user = self._add_user()
        dbfile = os.fdopen(self.handle)
        dbcontent = dbfile.read()
        self.assertIn('Johannes',dbcontent)
        self.assertIn('jmfrank63@gmail.com', dbcontent)

    def test_query_user(self):
        '''
        Test if an inserted user can be read from the database
        '''
        user = self._add_user()
        query_user = User.query.filter_by(email='jmfrank63@gmail.com').one()
        self.assertEqual(query_user, user)
        self.assertIn(query_user, db.session)

    def test_id_user(self):
        '''
        Tests if a user id stays with the user
        '''
        users = self._add_users()
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
        picture = MALE_IMAGE
        user_dict = {'id' : id,
                     'name' : name,
                     'email' : email,
                     'picture' : picture}
        user = self._add_user(User(name, email, picture))
        self.assertEqual(user.serialize, user_dict)

    def _add_language(self, language=None):
        '''
        Helper function inserting a default language into the database
        '''
        if language is None:
            language = Language('English')
        db.session.add(language)
        db.session.commit()
        return language

    def _add_languages(self):
        '''
        Adds several languages to the database
        '''
        languages = []
        languages.append(self._add_language(Language('French')))
        languages.append(self._add_language(Language('German')))
        languages.append(self._add_language(Language('Spanish')))
        languages.append(self._add_language(Language('Portuguese')))
        return languages

    def test_insert_language(self):
        '''
        Test if a language is inserted into the session
        '''
        language = self._add_language()
        self.assertEqual(language.name, 'English')

    def test_inserted_language(self):
        '''
        Test if the language is written into the database
        '''
        language = self._add_language()
        dbfile = os.fdopen(self.handle)
        dbcontent = dbfile.read()
        self.assertIn('English',dbcontent)

    def test_query_language(self):
        '''
        Test if an inserted language can be read from the database
        '''
        language = self._add_language()
        query_language = Language.query.filter_by(name='English').one()
        self.assertEqual(query_language, language)
        self.assertIn(query_language, db.session)

    def test_id_language(self):
        '''
        Tests if a user id stays with the user
        '''
        languages = self._add_languages()
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
        language = self._add_language(Language(name))
        self.assertEqual(language.serialize, language_dict)

    def _add_sentence(self, sentence=None):
        '''
        Helper function inserting a default sentence into the database
        '''
        if sentence is None:
            sentence = Sentence('Hello',
                                'Hello',
                                'file:///static/audio/hello.mp3',
                                1,
                                1)
        db.session.add(sentence)
        db.session.commit()
        return sentence

    def _add_sentences(self):
        '''
        Adds several sentences to the database
        '''
        sentences = []
        sentences.append(
            self._add_sentence(Sentence('Bonjour',
                                        'Hello',
                                        'file:///static/audio/bonjour.mp3',
                                        1,
                                        2)))
        sentences.append(
            self._add_sentence(Sentence('Guten Tag',
                                        'Hello',
                                        'file:///static/audio/guten_tag.mp3',
                                        1,
                                        3)))
        sentences.append(
            self._add_sentence(Sentence('Hombre',
                                        'Man',
                                        'file:///static/audio/hombre.mp3',
                                        1,
                                        4)))
        sentences.append(
            self._add_sentence(Sentence('Bem-vindo',
                                        'Welcome',
                                        'file:///static/audio/bem-vindo.mp3',
                                        1,
                                        5)))
        return sentences

    def test_insert_sentence(self):
        '''
        Test if a sentence is inserted into the session
        '''
        sentence = self._add_sentence()
        self.assertEqual(sentence.text, 'Hello')

    def test_inserted_sentence(self):
        '''
        Test if the sentence is written into the database
        '''
        sentence = self._add_sentence()
        dbfile = os.fdopen(self.handle)
        dbcontent = dbfile.read()
        self.assertIn('file:///static/audio/hello.mp3',dbcontent)

    def test_query_sentence(self):
        '''
        Test if an inserted sentence can be read from the database
        '''
        sentence = self._add_sentence()
        query_sentence = Sentence.query.filter_by(text='Hello').first()
        self.assertEqual(query_sentence, sentence)
        self.assertIn(query_sentence, db.session)

    def test_id_sentence(self):
        '''
        Tests if a user id stays with the user
        '''
        sentences = self._add_sentences()
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
        sentence = self._add_sentence(Sentence(text,
                                               translation,
                                               audio,
                                               user_id,
                                               lang_id))
        self.assertEqual(sentence.serialize, sentence_dict)

    def test_add_language_to_user(self):
        '''
        Tests if languages can be added to a user
        '''
        user = self._add_user()
        language = self._add_language()
        self.assertFalse(user.languages)
        user.languages.append(language)
        self.assertIn(language, user.languages)

    def test_user_in_added_language(self):
        '''
        Tests if a user is in language after adding the language to the user
        '''
        user = self._add_user()
        language = self._add_language()
        self.assertFalse(language.users)
        user.languages.append(language)
        self.assertIn(user, language.users)

    def test_add_languages_to_users(self):
        '''
        Test if multiple languages can be added to multiple users
        '''
        users = self._add_users()
        languages = self._add_languages()
        for user in users:
            for language in languages:
                user.languages.append(language)
        for user in users:
            for language in languages:
                self.assertIn(language, user.languages)
        for language in user.languages:
            for user in users:
                self.assertIn(user, language.users)

if __name__ == '__main__':
    main()
