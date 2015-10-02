#!/usr/bin/env python
''' Mangager script for flask. '''
from flask.ext.script import Manager, Shell, Server, Command
from werkzeug.contrib.fixers import ProxyFix

from os import getenv, system
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
    def run(self):
        '''
        Calls the test
        '''
        print 'Testing status codes:'
#        system('python ./atcatalog/views/test_pub_langs.py')
        testsuite = unittest.TestLoader().discover('.')
        unittest.TextTestRunner(verbosity=1).run(testsuite)

def main():
    '''The main entry point'''
    app.secret_key = SECRET
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = True
    manager = Manager(app)

    manager.add_command('run', Server(IP, PORT))
    manager.add_command('shell', Shell())
    manager.add_command('test', Test())
    manager.run()

if __name__ == '__main__':
    main()

