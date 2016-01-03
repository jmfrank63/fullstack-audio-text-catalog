# -*- coding: utf-8 -*-
'''
SqlAlchemy Model of the database
'''

from atcatalog import app
from flask.ext.sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.associationproxy import association_proxy

import sqlite3

from sqlalchemy.engine import Engine
from sqlalchemy import event

# For sqlite to force foreign key constraint
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:  # play well with other DB backends
       cursor = dbapi_connection.cursor()
       cursor.execute("PRAGMA foreign_keys=ON")
       cursor.close()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = u'sqlite:///data/atdatabase.db'
db = SQLAlchemy(app)

# helper table for many to many relationship of user and language
user_language = db.Table('user_language',
                            db.Column('user_id',db.Integer,
                                         db.ForeignKey('user.id')),
                            db.Column('lang_id', db.Integer,
                                         db.ForeignKey('language.id')))


class Language(db.Model):
    '''
    Language table
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    sentences = db.relationship('Sentence', backref='language', lazy='dynamic')

    def __init__(self, name):
        '''
        Passes language name and user to the language table object
        '''
        self.name = name


    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'id': self.id,
                 'name': self.name, }



class User(db.Model):
    '''
    User object holding id, name, email and list of languages
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    picture = db.Column(db.String(2000))
    lang_id = db.Column(db.ForeignKey('language.id'), nullable=False)
    languages = db.relationship("Language",
                                secondary=lambda: user_language,
                                backref="users")

    def __init__(self, name, email, picture=None, lang_id=1):
        '''
        Passes name and email to the table object
        '''
        self.name = name
        self.email = email
        self.picture = picture
        self.lang_id = lang_id

    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'id' : self.id,
                 'name' : self.name,
                 'email' : self.email,
                 'picture' : self.picture, }


class Sentence(db.Model):
    '''
    The Sentence class holding the sentence, the translation and the audio
    '''
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    translation = db.Column(db.Text)
    audio = db.Column(db.String(255))
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id'), nullable = False)
    lang_id = db.Column(db.Integer,
                        db.ForeignKey('language.id'), nullable = False)
    __table_args__ = (db.UniqueConstraint('text', 'user_id'),)

    def __init__(self, text, translation='',
                 audio='file:///static/audio/dummy.mp3',
                 user_id=1, lang_id=1):
        '''
        Passes text, translation and audio to the sentence object
        '''
        self.text = text
        self.translation = translation
        self.audio = audio
        self.user_id = user_id
        self.lang_id = lang_id

    @property
    def serialize(self):
        '''
        Returns an easy serializable format
        '''
        return { 'id' : self.id,
                 'text' : self.text,
                 'translation' : self.translation,
                 'audio' : self.audio,
                 'user_id' : self.user_id,
                 'lang_id' : self.lang_id }


if __name__ == '__main__':
    db.create_all()
