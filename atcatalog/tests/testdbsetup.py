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


class TestLanguage(TestCase):
    '''
    Basic testing of the language site
    '''
    def create_app(self):
        '''
        Necessary for the flask testing extension module
        '''
        app.config['TESTING'] = True
        self.handle, self.dbname = mkstemp(suffix='.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.dbname
                                                
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
        os.close(self.handle)
        os.remove(self.dbname)

    def test_insert_user(self):
        '''
        Tests if a user is actually inserted into the database
        '''
        user = User('Johannes', 'jmfrank63@gmail.com', 'image.jpg')
        db.session.add(user)
        db.session.commit()
        self.assertIn(user, db.session)


if __name__ == '__main__':
    main()
