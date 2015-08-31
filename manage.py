#!/usr/bin/env python
''' Mangager script for flask. '''
# from flask.ext.script import Manager, Shell, Server
from flask_script import Manager, Shell, Server
from os import getenv
from atcatalog import app


# get server address from environment
IP = getenv('IP', '0.0.0.0')
PORT = getenv('PORT', '8080')


def main():
    '''The main entry point'''
    manager = Manager(app)

    manager.add_command('run', Server(IP, PORT))
    manager.add_command('shell', Shell())
    manager.run()

if __name__ == '__main__':
    main()

