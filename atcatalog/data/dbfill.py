# -*- coding: utf-8 -*-
'''
This module provides helper functions filling the database with entries
'''
from atcatalog.data.dbsetup import db, User, Language, Sentence, user_language
import atcatalog.data.const as const


def add_user(user=None):
    '''
    Helper function inserting a default user into the database
    '''
    if user is None:
        user = User('Johannes', 'jmfrank63@gmail.com',
                    const.MALE_IMAGE)
    db.session.add(user)
    db.session.commit()
    return user

def add_users():
    '''
    Adds several users to the database
    '''
    users = []
    users.append(add_user(User('Ted', 'ted@example.com', 
                               const.MALE_IMAGE)))
    users.append(add_user(User('Jane', 'janedoe@example.com', 
                               const.FEMALE_IMAGE)))
    users.append(add_user(User('John', 'johndoe@example.com',
                               const.MALE_IMAGE)))
    users.append(add_user(User('Sarah', 'sarah@example.com',
                               const.FEMALE_IMAGE)))
    return users

def add_language(language=None):
    '''
    Helper function inserting a default language into the database
    '''
    if language is None:
        language = Language('English')
    db.session.add(language)
    db.session.commit()
    return language

def add_languages():
    '''
    Adds several languages to the database
    '''
    languages = []
    languages.append(add_language(Language('French')))
    languages.append(add_language(Language('German')))
    languages.append(add_language(Language('Spanish')))
    languages.append(add_language(Language('Portuguese')))
    return languages

def add_sentence(sentence=None):
    '''
    Helper function inserting a default sentence into the database
    '''
    if sentence is None:
        sentence = Sentence('Hello',
                            'Hello',
                            'file:///static/audio/hello.mp3',
                            1,
                            1)
    db.session.add(sentence)
    db.session.commit()
    return sentence

def add_sentences():
    '''
    Adds several sentences to the database
    '''
    sentences = []
    sentences.append(
        add_sentence(Sentence('Bonjour',
                                    'Hello',
                                    'file:///static/audio/bonjour.mp3',
                                    1,
                                    2)))
    sentences.append(
        add_sentence(Sentence('Guten Tag',
                                    'Hello',
                                    'file:///static/audio/guten_tag.mp3',
                                    1,
                                    3)))
    sentences.append(
        add_sentence(Sentence('Hombre',
                                    'Man',
                                    'file:///static/audio/hombre.mp3',
                                    1,
                                    4)))
    sentences.append(
        add_sentence(Sentence('Bem-vindo',
                                    'Welcome',
                                    'file:///static/audio/bem-vindo.mp3',
                                    1,
                                    5)))
    return sentences
