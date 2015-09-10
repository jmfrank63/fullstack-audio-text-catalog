#!/usr/bin/env python
''' Mangager script for flask. '''
# from flask.ext.script import Manager, Shell, Server
from flask_script import Manager, Shell, Server
from werkzeug.contrib.fixers import ProxyFix

from os import getenv
from atcatalog import app


# get server address from environment
IP = getenv('IP', '0.0.0.0')
PORT = getenv('PORT', '8080')
SECRET = getenv('FLASK_SECRET', 'udacity_super_secret_key')

def main():
    '''The main entry point'''
    app.secret_key = SECRET
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = True
    manager = Manager(app)

    manager.add_command('run', Server(IP, PORT))
    manager.add_command('shell', Shell())
    manager.run()

if __name__ == '__main__':
    main()

