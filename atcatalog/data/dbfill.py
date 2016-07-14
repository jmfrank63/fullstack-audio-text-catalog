# -*- coding: utf-8 -*-
'''
This module provides helper functions filling the database with entries
'''
from atcatalog.model.atcmodel import *
from atcatalog.data.gendata import *
from atcatalog.data.const import *

def add_all_languages():
    '''
    Adds all languages to the database
    '''
    db.session.add_all([Language(code) for code in create_all_codes()])
    db.session.commit()

def add_users(num):
    '''
    Adds num users to the database
    '''
    for _ in xrange(USER_NUM):
        codes = create_random_codes(random.randint(1,len(LANG_DICT)))
        user = create_random_user(codes)
        db.session.add(user)
        db.session.commit()

def add_sentences(num):
    '''
    Adds up randomly from one to num sentences for each user to the database
    '''
    for user in User.query.all():
        for code in user.languages:
            db.session.add_all([create_random_sentence(code, user)
                                for _ in
                                xrange(random.randint(1,SENTENCE_NUM))])
            db.session.commit()

def dbfill(user_num, sentence_num):
    '''
    Fills the database with languages, users and sentences
    '''
    atcmodel()
    add_all_languages()
    add_users(user_num)
    add_sentences(sentence_num)


if __name__ == '__main__':
    dbfill(USER_NUM, SENTENCE_NUM)