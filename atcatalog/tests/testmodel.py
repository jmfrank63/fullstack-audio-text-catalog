# -*- coding: utf-8 -*-
'''
Test cases for the database model
'''
from atcatalog import app
from unittest import main
from flask.ext.testing import TestCase

from tempfile import mkstemp

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
        self.db_id, app.config['DATABASE'] = mkstemp()
        print self.db_id, app.config['DATABASE']
        return app

    def setUp(self):
        '''
        Setup the database
        '''
        self.id

    def tearDown(self):
        '''
        Drop all tables in the database so we can start again
        '''
        pass


if __name__ == '__main__':
    main()
