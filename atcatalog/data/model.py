# -*- coding: utf-8 -*-
'''
SqlAlchemy Model of the database
'''

from atcatalog import app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = u'sqlite:////tmp/test.db'
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
    name = db.Column(db.String(80), nullable=False)
    user = db.relationship('User',secondary=lambda: user_language,
                              backref=db.backref('users',
                                                 lazy='dynamic'))
    users = association_proxy('user','name')
    sentences = db.relationship('Sentence', backref='language', lazy='dynamic')

    def __init__(self, name):
        '''
        Passes language name and user to the language table object
        '''
        self.name = name

    def __str__(self):
        '''
        Defines the representation of the object
        '''
        return 'Id: {0},\n Name: {1}'.format(self.id, self.name)


    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'id': self.id,
                 'lname': self.name, }


class User(db.Model):
    '''
    User object holding id, name, email and list of languages
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    picture = db.Column(db.BLOB)
    language = db.relationship('Language',
                                secondary=lambda: user_language,
                                backref=db.backref('languages',
                                                   lazy='dynamic'))
    languages = association_proxy('language', 'lname')
    sentences = db.relationship('Sentence',backref='user', lazy='dynamic')


    def __init__(self, name, email, picture):
        '''
        Passes name and email to the table object
        '''
        self.name = name
        self.email = email
        self.picture = picture

    def __str__(self):
        return 'Id: {0},\n \
                User: {1},\n \
                email: {2},\n \
                Picture: {3}'.format(self.id,
                                     self.name,
                                     self.email,
                                     self.picture)

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lang_id = db.Column(db.Integer, db.ForeignKey('language.id'))

    def __init__(self, text, translation='', audio='dummy.mp3'):
        '''
        Passes text, translation and audio to the sentence object
        '''
        self.text = text
        self.translation = translation
        self.audio = audio

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
