# -*- coding: utf-8 -*-
'''
This module provided generating functions for data for testing. It uses the
orm objects from sqlalchemy.
'''
import faker
import random
from atcatalog.data.const import *
from atcatalog.model.atcmodel import *


# The language section *******
def create_random_code():
    '''
    Returns a random language code
    '''
    return random.choice(LANG_DICT.keys())

def create_random_codes(num):
    '''
    Creates a list of language codes in random order
    '''
    codes = LANG_DICT.keys()
    random.shuffle(codes)
    if num >= len(codes):
        return codes
    return codes[:num]

def create_all_codes():
    '''
    Creates all languages
    '''
    return LANG_DICT.keys()

    # The users section **********
def create_random_user_data(codes):
    '''
    Creates a random user
    with a list of languages
    '''
    fake = faker.Factory.create(codes[0])
    name = fake.name()
    email = fake.email()
    picture = IMAGE
    user_data = [name, email, codes, picture]
    return user_data

# The sentence section ********
def create_random_sentence_data(lid, uid):
    '''
    Generates a random sentence of a given user and language code
    If language code is not given the first language code of the user
    is used.
    '''
    code = random.choice(LANG_DICT.keys())
    fake = faker.Factory.create(code)
    text = fake.sentence()
    translation = fake.sentence()
    audio = AUDIO_DUMMY
    sentence_data = [text, translation, audio, lid, uid]
    return sentence_data

if __name__ == '__main__':
    pass
