# -*- coding:utf-8 -*-
'''
Test module for one to many relationship
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import pprint


from sqlalchemy import Column, Integer, String
Base = declarative_base()
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
    def __init__(self, name, fullname, password):
        '''User init funciton'''
        self.name = name
        self.fullname = fullname
        self.password = password

def declare():
    '''The init function'''
    return create_engine('sqlite:///:memory:', echo=True)
    

if __name__ == '__main__':
    engine = declare()
    
