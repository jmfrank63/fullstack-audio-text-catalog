# -*- coding: utf-8 -*-
'''
This module provides helper functions filling the database with entries
It mainly consists of there functions filling in
languages
users
sentences
'''
from atcatalog.model.atcmodel import *
from atcatalog.data.gendata import *
from atcatalog.data.const import *
from random import randint

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
    for _ in xrange(num):
        codes = create_random_codes(randint(1,len(LANG_DICT)))
        user = User(*create_random_user_data(codes))
        db.session.add(user)
        db.session.commit()

def add_sentences(num):
    '''
    Adds a random number of  sentences for each user to the database

    '''
    for user in User.query.all():
        for language in user.languages:
            sentences = [Sentence(*create_random_sentence_data(language.id,
                                                               user.id))
                         for _ in xrange(randint(1,num))
                        ]
            db.session.add_all(sentences)
            db.session.commit()

def dbfill(user_num, sentence_num):
    '''
    Fills the database with languages, users and sentences
    '''
    atcmodel(True)
    add_all_languages()
    add_users(user_num)
    add_sentences(sentence_num)


if __name__ == '__main__':
    dbfill(USER_NUM, SENTENCE_NUM)