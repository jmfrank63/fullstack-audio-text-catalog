# -*- coding: utf-8 -*-
'''
This module provides an abstraction layer for manipulating data in the database
'''
from atcatalog.data.dbsetup import db, make_db, User, Language, Sentence
from atcatalog.data.gendata import GenDBData
import atcatalog.data.const as const
from pprint import pprint


def add_language(language):
    '''
    Adds a language to the database if it does not exist
    '''
    if Language.query.filter_by(code=language.code).one_or_none() is None:
        db.session.add(language)
        db.session.commit()
        
def change_language(language, new_language):
    '''
    Changes a language in the database
    '''
    language = Language.query.filter_by(code=language.code).one()
        
def remove_language(language):
    '''
    Removes a language from the database
    '''
    
def add_complete_user(complete_user):
    '''
    Adds a complete user to the database
    Throws an error if the user is not complete
    '''
    
def change_complete_user(complete_user, new_complete_user):
    '''
    Changes a user in the database
    Throws an error if user or new user aren't complete
    '''
    
def remove_user(user):
    '''
    Removes a user from the database
    '''
    
def complete_user(user, language, languages):
    '''
    Adds native language and list of additional languages
    so the user can be inserted into the database
    '''
    
def add_sentence(complete_sentence):
    '''
    Adds a sentence to the database
    '''
    
def change_complete_sentence(sentence, new_sentence):
    '''
    Changes a sentence in the database
    '''
    
def remove_sentence(sentence):
    '''
    Removes a sentence from the database
    '''

def complete_sentence(sentence, language, user):
    '''
    Adds language and user to a sentence so it can
    be inserted into the database
    '''
    
if __name__ == '__main__':
    data = GenDBData(0,5,1)
    pprint([lang.serialize for lang in data.languages])
    pprint([user.serialize for user in data.users])
    pprint([sentence.serialize for sentence in data.sentences])