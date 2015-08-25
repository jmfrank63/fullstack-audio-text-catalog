#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server
from os import getenv
from atcatalog import app


# get server address from environment
ip = getenv('IP', '0.0.0.0')
port  = getenv('PORT', '8080')


# create manager
manager = Manager(app)

manager.add_command('run', Server(ip, port) )
manager.add_command('shell', Shell())


if __name__ == '__main__':
    manager.run()

