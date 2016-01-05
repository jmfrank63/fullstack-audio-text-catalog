# -*- coding: utf-8 -*-
'''
Main project flask file for the audio text catalog
'''
from flask import Flask
from sqlalchemy.engine import Engine
from sqlalchemy import event
import sqlite3

# For sqlite to force foreign key constraint
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:  # play well with other DB backends
       cursor = dbapi_connection.cursor()
       cursor.execute("PRAGMA foreign_keys=ON")
       cursor.close()
app = Flask(__name__)

import atcatalog.views.languages
import atcatalog.views.language
import atcatalog.views.sentence
