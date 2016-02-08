# -*- coding:utf-8 -*-
'''
Test module for one to many relationship
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from pprint import pprint
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)


class User(Base):
    '''User class'''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', password='{2}')>".\
                format(self.name, self.fullname, self.password)

def schema():
    '''
    Base function
    '''
    Base.metadata.create_all(engine)
    user = User(name='John', fullname='John Doe', password='johnspassword')
    pprint(user)
    pprint(User.__table__)

if __name__ == '__main__':
    schema()

