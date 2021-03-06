# -*- coding: utf-8 -*-
'''
SqlAlchemy Model of the database
'''

from atcatalog import app
from ormhelper import *
from atcatalog.data.const import *
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.engine import Engine
from sqlalchemy import event, UniqueConstraint
from sqlite3 import Connection
import os

# For sqlite to force foreign key constraint
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    '''
    Sets the foreign key constraint for sqlite3
    '''
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# set config parameters and set up database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)



#helper table for many to many relationship of user and language
user_language =\
    db.Table('user_language',
             db.Column('user',db.Integer, db.ForeignKey('user.id'), primary_key=True),
             db.Column('language', db.Integer, db.ForeignKey('language.id'), primary_key=True))

class LanguageDetails(db.Model):
    '''
    Language text names
    '''
    code = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String, nullable=False)


class Language(UniqueMixin, db.Model):
    '''
    Language table as unique class
    '''
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), db.ForeignKey('language_details.code'))
    details = db.relationship('LanguageDetails', uselist=False)
    name = association_proxy('details', 'name')
    sentences = db.relationship('Sentence', backref='language')

    @classmethod
    def unique_hash(cls, code):
        return code

    @classmethod
    def unique_filter(cls, query, code):
        return query.filter(Language.code == code)

    def __init__(self, code):
        '''
        Passes language code to the language table object
        '''
        self.code = code

    @force_encoded_string_output
    def __repr__(self):
        '''
        String representing the object
        '''
        return u"<Language(id={}, code='{}')>".format(self.id, self.code)

    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'id': self.id,
                 'code': self.code}


class User(UserMixin, db.Model):
    '''
    User object holding id, name, email and list of languages
    '''
    def _lang_code(code):
        return Language.as_unique(db.session, code=code)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    picture = db.Column(db.String(2000))
    languages = db.relationship('Language',
                                secondary=lambda: user_language,
                                backref='users')
    codes = association_proxy('languages', 'code', creator=_lang_code)
    sentences = db.relationship('Sentence', backref='user')

    def __init__(self, name, email, codes, picture):
        '''
        Initializes the user object
        '''
        self.name = name
        self.email = email
        self.codes.extend(codes)
        self.picture = picture

    @force_encoded_string_output
    def __repr__(self):
        '''
        Pretty print of the object
        '''
        return u"<User(id={}, name='{}', email='{}', codes='{}', \
picture='{}', languages='{}', sentences='{}')>".format(self.id,
                                                       self.name,
                                                       self.email,
                                                       self.codes,
                                                       self.picture,
                                                       self.languages,
                                                       self.sentences)

    @property
    def serialize(self):
        '''
        Returns object data in an easy serializable format
        '''
        return { 'id': self.id,
                 'name': self.name,
                 'email': self.email,
                 'codes' : self.codes,
                 'picture': self.picture,
                 'languages': self.languages,
                 'sentences' : self.sentences }


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
    language_id = db.Column(db.Integer,
                        db.ForeignKey('language.id'), nullable = False)

    __table_args__ = (db.UniqueConstraint('text', 'user_id'),)

    def __init__(self, text, translation, audio, language_id, user_id):
        '''
        Passes text, translation and audio to the sentence object
        '''
        self.text = text
        self.translation = translation
        self.audio = audio
        self.language_id = language_id
        self.user_id = user_id


    @force_encoded_string_output
    def __repr__(self):
        '''
        Pretty print of the object
        '''
        return u"<Sentence(id={}, text='{}', translation='{}', audio='{}', \
language_id='{}', user_id='{}')>".format(self.id,
                                          self.text,
                                          self.translation,
                                          self.audio,
                                          self.language_id,
                                          self.user_id)

    @property
    def serialize(self):
        '''
        Returns an easy serializable format
        '''
        return { 'id' : self.id,
                 'text' : self.text,
                 'translation' : self.translation,
                 'audio' : self.audio,
                 'language_id' : self.language_id,
                 'user_id' : self.user_id }

def atcmodel():
    '''
    creates the database
    '''
    db.create_all()

if __name__ == '__main__':
    atcmodel()
