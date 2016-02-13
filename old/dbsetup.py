# -*- coding: utf-8 -*-
'''
SqlAlchemy Model of the database
'''

from atcatalog import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = u'sqlite:///data/atdatabase.db'
db = SQLAlchemy(app)

# helper table for many to many relationship of user and language
user_language = db.Table('user_language',
                            db.Column('user',db.Integer,
                                         db.ForeignKey('user.id')),
                            db.Column('language', db.Integer,
                                         db.ForeignKey('language.id')))


class Language(db.Model):
    '''
    Language table
    '''
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), nullable=False, unique=True)
    sentences = db.relationship('Sentence', backref='language', lazy='dynamic')

    def __init__(self, code):
        '''
        Passes language code to the language table object
        '''
        self.code = code

    def __repr__(self):
        '''
        String representing the object
        '''
        return u'Language id: {0}, code: {1}'.format(self.id, self.code)

    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'id': self.id,
                 'code': self.code }


class User(db.Model):
    '''
    User object holding id, name, email and list of languages
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    picture = db.Column(db.String(2000))
    language = db.Column(db.ForeignKey('language.id'), nullable=False)
    languages = db.relationship("Language",
                                secondary=lambda: user_language,
                                backref="users")

    def __init__(self, name, email, picture, language, languages):
        '''
        Initializes the user object
        '''
        self.name = name
        self.email = email
        self.picture = picture
        self.lang_id = add_language(language).id
        self.language = language

    @property
    def serialize(self):
        '''
        Returns object data in an easy serializable format
        '''
        language = Language.query.get(language)
        languages = [(lang.id, lang.code)
                     for lang in Language.query.get(lng.id)
                         for lng in self.languages]
        return { 'id': self.id,
                 'name': self.name,
                 'email': self.email,
                 'picture': self.picture,
                 'language': (language.id, language.code),
                 'languages': languages}


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

    def __init__(self, text, translation, audio, user_id, language_id):
        '''
        Passes text, translation and audio to the sentence object
        '''
        self.text = text
        self.translation = translation
        self.audio = audio
        self.user_id = user_id
        self.language_id = language_id

    @property
    def serialize(self):
        '''
        Returns an easy serializable format
        '''
        return { 'id' : self.id,
                 'text' : self.text,
                 'translation' : self.translation,
                 'audio' : self.audio,
                 'user' : self.user_id,
                 'language' : self.language_id }

def make_db():
    '''
    creates the database
    '''
    db.create_all()

if __name__ == '__main__':
    make_db()