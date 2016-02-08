# -*- coding: utf-8 -*-
'''
SqlAlchemy Model of the database
'''
from __future__ import unicode_literals, print_function
from atcatalog import app
from flask.ext.sqlalchemy import SQLAlchemy, SignallingSession
from sqlalchemy.ext.associationproxy import association_proxy
import atcatalog.data.const as const
from sqlalchemy.engine import Engine
from sqlalchemy import event
import sqlite3
import sys

# For sqlite to force foreign key constraint
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # play well with other DB backends
    if type(dbapi_connection) is sqlite3.Connection:
       cursor = dbapi_connection.cursor()
       cursor.execute("PRAGMA foreign_keys=ON")
       cursor.close()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = const.DB_URI
db = SQLAlchemy(app)

# Taken from
# http://code.activestate.com/recipes/
# 466341-guaranteed-conversion-to-unicode-or-byte-string/
def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

def force_encoded_string_output(func):
    '''
    Decorator taken from:
    http://stackoverflow.com/questions/3627793/
    best-output-type-and-encoding-practices-for-repr-functions
    to have encoded __repr__
    '''
    if sys.version_info.major < 3:
        def _func(*args, **kwargs):
            return func(*args, **kwargs).encode(sys.stdout.encoding or 'utf-8')
        return _func
    else:
        return func

def _unique(session, cls, hashfunc, queryfunc, constructor, arg, kw):
    cache = getattr(session, '_unique_cache', None)
    if cache is None:
        session._unique_cache = cache = {}

    key = (cls, hashfunc(*arg, **kw))
    if key in cache:
        return cache[key]
    else:
        with session.no_autoflush:
            q = session.query(cls)
            q = queryfunc(q, *arg, **kw)
            obj = q.first()
            if not obj:
                obj = constructor(*arg, **kw)
                session.add(obj)
        cache[key] = obj
        return obj

def unique_constructor(session, hashfunc, queryfunc):
    def decorate(cls):
        def _null_init(self, *arg, **kw):
            pass
        def __new__(cls, bases, *arg, **kw):
            # no-op __new__(), called
            # by the loading procedure
            if not arg and not kw:
                return object.__new__(cls)

            def constructor(*arg, **kw):
                obj = object.__new__(cls)
                obj._init(*arg, **kw)
                return obj

            return _unique(
                        session,
                        cls,
                        hashfunc,
                        queryfunc,
                        constructor,
                        arg, kw
                   )

        # note: cls must be already mapped for this part to work
        cls._init = cls.__init__
        cls.__init__ = _null_init
        cls.__new__ = classmethod(__new__)
        return cls

    return decorate

# helper table for many to many relationship of user and language
user_language =\
    db.Table('user_language',
             db.Column('user',db.Integer, db.ForeignKey('user.id')),
             db.Column('language', db.Integer, db.ForeignKey('language.id')))

# @unique_constructor(db.session,
#                     lambda code: code,
#                     lambda query, code: query.filter(Language.code == code)
# )
class Language(db.Model):
    '''
    Language table
    '''
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), nullable=False, unique=True)
    sentences = db.relationship('Sentence', backref='language')

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
        return u"<Language(id={0}, code='{1}')>\n\t".format(self.id, self.code)

    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'id': self.id,
                 'code': self.code }


@unique_constructor(db.session,
                    lambda code: code,
                    lambda query, code: query.filter(Language.code == code)
)
class UniqueLanguage(Language):
    '''
    The language class with unique enforced members
    '''

class User(db.Model):
    '''
    User object holding id, name, email and list of languages
    '''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    picture = db.Column(db.String(2000))
    languages = db.relationship('Language',
                                secondary=lambda: user_language,
                                backref='users')
    codes = association_proxy('languages', 'code')
    sentences = db.relationship('Sentence', backref='user')

    def __init__(self, name, email, codes=[],
                 picture=const.MALE_IMAGE):
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
        return u"<User(id={},\n\
    name='{}',\n\
    email='{}',\n\
    codes='{}',\n\
    picture='{}',\n\
    languages = '{}',\n\
    sentences='{}'>  \n".format(self.id,
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
                 'picture': self.picture,
                 'languages': self.languages,
                 'codes' : self.codes,
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
        return u"<User(id={},\n\
      text='{}',\n\
      translation='{}',\n\
      audio='{}',\n\
      language_id='{}',\n\
      user_id='{}'>\n".format(self.id,
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
