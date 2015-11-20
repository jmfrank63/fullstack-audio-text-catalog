#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Mangager script for flask. '''
from flask.ext.script import Manager, Shell, Server, Command, Option
from werkzeug.contrib.fixers import ProxyFix
from coverage import coverage
from os import getenv, system, path
from atcatalog import app

import unittest

# get server address from environment
IP = getenv('IP', '0.0.0.0')
PORT = getenv('PORT', '8080')
SECRET = getenv('FLASK_SECRET', 'udacity_super_secret_key')

class Test(Command):
    '''
    Runs the tests
    '''
    option_list = (
        Option('--verbosity', '-v', dest='verbosity'),
    )
    def run(self, verbosity=1):
        '''
        Calls the test
        '''
        testsuite = unittest.TestLoader().discover('atcatalog')
        unittest.TextTestRunner(verbosity=verbosity).run(testsuite)

class Cover(Command):
    '''
    Runs the cover test
    '''
    def run(self):
        '''
        Calls the coverage command
        '''
        system('coverage erase && coverage run -m unittest discover')
        system('coverage html && coverage report -m')


def main():
    '''
    The main entry point
    '''
    app.secret_key = SECRET
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = True
    manager = Manager(app)

    manager.add_command('cover', Cover())
    manager.add_command('test', Test())
    manager.add_command('shell', Shell())
    manager.run()

if __name__ == '__main__':
    main()

