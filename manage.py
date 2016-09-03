#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Mangager script for flask.
'''
from flask.ext.script import Manager, Shell, Server, Command, Option
from werkzeug.contrib.fixers import ProxyFix
from coverage import coverage
from os import getenv, environ, system, path, rename
from atcatalog import app
from atcatalog.model.atcmodel import *
from atcatalog.data.const import *
from atcatalog.data.dbfill import *

import unittest

# get server address from environment
IP = getenv('IP', '0.0.0.0')
PORT = getenv('PORT', '8080')
SECRET = getenv('FLASK_SECRET', 'udacity_super_secret_key')

class Test(Command):
    '''
    Run an individual test
    '''
    option_list = (
        Option('--name', '-n', dest='name', required=True),
        Option('--module', '-m', dest='module', default=None),
        Option('--verbosity', '-v', dest='verbosity', default=2),
    )
    def run(self, name, module, verbosity):
        '''
        Execute the command
        '''
        testsuite = unittest.TestLoader().loadTestsFromName(name, module)
        unittest.TextTestRunner(verbosity=verbosity).run(testsuite)

class AllTests(Command):
    '''
    Discover all tests and run them
    '''
    option_list = (
        Option('--verbosity', '-v', dest='verbosity', default=2),
        Option('--filltest', '-f', dest='filltest', default='FALSE'),
    )
    def run(self, verbosity, filltest):
        '''
        Execute the command
        '''
        TEST_FILL = getenv('TEST_FILL', 'FALSE')
        if filltest.upper() == 'TRUE':
            TEST_FILL = 'TRUE'

        testsuite = unittest.TestLoader().discover('atcatalog')
        unittest.TextTestRunner(verbosity=verbosity).run(testsuite)

class Coverage(Command):
    '''
    Runs test coverage
    '''
    option_list = (
        Option('--filltest', '-f', dest='filltest', default='FALSE'),
    )
    def run(self, filltest):
        '''
        Execute the command
        '''
        TEST_FILL = getenv('TEST_FILL', 'FALSE')
        if filltest.upper() == 'TRUE':
            TEST_FILL = 'TRUE'

        system('coverage erase && coverage run -m unittest discover')
        system('coverage html && coverage report -m')

class NewDataBase(Command):
    '''
    Creates a new database
    '''
    option_list = (
        Option('--users', '-u', dest='users', default=USER_NUM),
        Option('--sentences', '-s', dest='sentences', default=SENTENCE_NUM),
    )
    def run(self, users, sentences):
        '''
        Execute the comand
        '''
        FILE_PATH = DB_PATH + DB_FILE
        if os.path.exists(FILE_PATH):
            rename(FILE_PATH, FILE_PATH + '.backup')
        dbfill(int(users), int(sentences))


def _make_shell_context():
    return dict(app=app, db=db, LanguageDetails=LanguageDetails,
                Language=Language, User=User, Sentence=Sentence)

def main():
    '''
    The main entry point
    '''
    app.secret_key = SECRET
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = True
    manager = Manager(app)

    manager.add_command('test', Test())
    manager.add_command('coverage', Coverage())
    manager.add_command('alltests', AllTests())
    manager.add_command('shell', Shell(make_context=_make_shell_context))
    manager.add_command('newdb', NewDataBase())
    manager.run()

if __name__ == '__main__':
    main()
