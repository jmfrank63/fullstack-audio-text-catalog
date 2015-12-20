# -*- coding: utf-8 -*-
'''
Test cases for the database model
'''
from atcatalog import app
from atcatalog.data.dbsetup import db, User, Language, Sentence
from unittest import main
from flask.ext.testing import TestCase
from tempfile import mkstemp
import os

__author__ = 'Johannes Maria Frank'

DB_PREFIX = 'sqlite:///'
MALE_IMAGE = 'file:///static/images/male.png'
FEMALE_IMAGE = 'file:///static/images/female.png'

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

    def _add_languges(self):
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
        languages = self._add_languges()
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

if __name__ == '__main__':
    main()
