# -*- coding:utf-8 -*-
'''
This module contains functions to access the database
'''

from atcatalog.model.atcmodel import *

def add_language(code, commit=True):
    '''
    Creates a language and if it not exists inserts it into the database
    '''
    lang = Language.query.filter_by(code=code).one_or_none()
    if lang:
        return lang
    lang = Language(code)
    db.session.add(lang)
    if commit:
        db.session.commit()
    return lang

def update_language(old_code, new_code, commit=True):
    '''
    Changes the code of a language
    Throws an error if the language does not exist
    '''
    lang = Language.query.filter_by(code=old_code).one()
    lang.code = new_code
    if commit:
        db.session.commit()

def get_language_by_code(code):
    '''
    Returns the language object for the code
    '''
    return Language.query.filter_by(code=code).one()

def get_language_by_id(id):
    '''
    Returns the language object for the code
    '''
    return Language.query.get(id)

def remove_language_by_code(code):
    '''
    Removes a language object by its code
    '''
    lang = get_language_by_code(code)
    db.session.delete(lang)
    db.session.commit()

def remove_language_by_id(code, commit=True):
    '''
    Removes a language by id
    '''
    lang = get_language_by_id(id)
    db.session.delete(lang)
    if commit:
        db.session.commit()

def atcaccess():
    '''
    Function for standalone call
    '''
    atcmodel()

if __name__ == '__name__':
    atcaccess()