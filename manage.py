#!/usr/bin/env python
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
        testsuite = unittest.TestLoader().discover('atcatalog/tests')
        unittest.TextTestRunner(verbosity=verbosity).run(testsuite)

class Cover(Command):
    '''
    Runs the cover test
    '''
    def run(self):
        '''
        Calls the cover command
        '''
        cover = coverage(branch=True, include='atcatalog/*')
        cover.start()
        test = Test()
        test.run(1)
        cover.stop()
        cover.save()
        print 'Coverage Summary:'
        cover.report()
        basedir = path.abspath(path.dirname(__file__))
        covdir = path.join(basedir, 'coverage')
        cover.html_report(directory=covdir)
        cover.erase()


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

