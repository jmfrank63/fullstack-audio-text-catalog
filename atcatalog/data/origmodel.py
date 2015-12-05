# -*- coding: utf-8 -*-
''' Setup a database structure
'''
__author__ = 'Johannes Maria Frank'

from sqlalchemy import Column, ForeignKey, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

######################################################
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    picture = Column(BLOB)

    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'id' : self.id,
                 'name' : self.name,
                 'email' : self.email,
                 'picture' : self.picture, }


class Language(Base):
    __tablename__ = 'language'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'name': self.name,
                 'id': self.id,
                 'user_id': self.user_id, }


class Sentence(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    text = Column(String(250))
    translation = Column(String(250))
    audio = Column(BLOB)
    language_id = Column(Integer, ForeignKey('language.id'))
    language = relationship(Language)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        ''' Returns object data in an easy serializable format
        '''
        return { 'name' : self.name,
                 'text' : self.text,
                 'id' : self.id,
                 'audio' : self.audio,
                 'translation' : self.translation,
                 'language_id' : self.language_id,
                 'user_id' : self.user_id }

################### insert at end of file ############

engine = create_engine('sqlite:///language.db')
Base.metadata.create_all(engine)

