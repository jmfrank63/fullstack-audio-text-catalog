# -*- coding: utf-8 -*-
'''
This module generates data for testing. It uses the
orm objects from sqlalchemy.
Since we generate the objects without writing them
into the database we do not have any ids available. Therefore
any attribute that is meant to hold a foreign key integer
holds the full object instead.
'''
import faker
import csv
import random
import atcatalog.data.const as const
from atcatalog.model.atcmodel import *
from sqlalchemy.ext.hybrid import hybrid_property


class GenLanguage(Language):
    '''
    Generated language works without the database
    '''
    def __init__(self, code):
        super(GenLanguage, self).__init__(code)

    @force_encoded_string_output
    def __repr__(self):
        '''
        String representing the object
        '''
        return u"<Language(code='{}')>\n".format(self.code)

class GenUser(User):
    '''
    Generated user works without the database
    '''
    def __init__(self, *args, **kwargs):
        super(GenUser, self).__init__(*args, **kwargs)
        self._sentences = []

    @property
    def sentences(self):
        return self._sentences

    @sentences.setter
    def sentences(self, value):
        self._sentences.extend(value)

    @force_encoded_string_output
    def __repr__(self):
        '''
        Pretty print of the object
        '''
        return u"\n<User(name='{}',\n\
    email='{}',\n\
    codes='{}',\n\
    picture='{}',\n\
    sentences='{}'>".format(self.name,
                            self.email,
                            self.codes,
                            self.picture,
                            repr(self._sentences).decode('utf-8'))


class GenSentence(Sentence):
    '''
    Generated sentence works without the database
    '''
    def __init__(self, text, translation, audio,
                 code, email):
        super(GenSentence, self).__init__(text, translation, audio,
                                          1, 1)
        self.code = code
        self.email = email

    @force_encoded_string_output
    def __repr__(self):
        '''
        Pretty print of the object
        '''
        return u"<User(text='{}',\n\
      translation='{}',\n\
      audio='{}',\n\
      code='{}',\n\
      email='{}'> \n".format(self.text,
                            self.translation,
                            self.audio,
                            self.code,
                            self.email)

# The language section *******
def create_random_code():
    '''
    Returns a random language code
    '''
    return random.choice(list(const.LANG_DICT.keys()))

def create_random_codes(num=const.LANG_NUM):
    '''
    Creates a list of language codes in random order
    '''
    codes = list(const.LANG_DICT.keys())
    random.shuffle(codes)
    if num >= len(codes):
        return codes
    return codes[:num]

def create_all_codes():
    '''
    Creates all languages
    '''
    return [GenLanguage(code) for code in const.LANG_DICT.keys()]

    # The users section **********
def create_random_user(code=None):
    '''
    Creates a random user
    '''
    if code is None:
        code = create_random_code()
    fake = faker.Factory.create(code)
    name = fake.name()
    email = fake.email()
    picture = const.IMAGE
    lang_num = random.randint(0, len(const.LANG_DICT))
    codes = create_random_codes(lang_num)
    if code in codes:
        codes.remove(code)
    codes[:0] = [code]
    user = GenUser(name, email, codes, picture)
    return user

def create_random_users(num=const.USER_NUM):
    '''
    Creates a list of random users
    '''
    return [create_random_user() for _ in range(num)]


# The sentence section ********
def create_random_sentence(user, code=None):
    '''
    Generates a random sentence of a given user and language code
    If language code is not given the first language code of the user
    is used.
    '''
    if code is None:
        code = user.codes[0]
    if code not in user.codes:
        user.codes.append(code)
    fake = faker.Factory.create(code)
    text = fake.sentence()
    translation = fake.sentence()
    audio = const.AUDIO_DUMMY
    sentence = GenSentence(text, translation, audio, code, user.email)
    return sentence

def create_random_sentences(user=None, code=None, num=const.SENTENCE_NUM):
    '''
    Creates a list of random sentences of a given user and language code
    If user is not given a random user is used if language code is not given
    the first language code of the user is used.
    '''
    if user is None:
        user = create_random_user()
    if code is None:
        code = user.codes[0]
    if code not in user.codes:
        user.codes.append(code)
    return [create_random_sentence(user, code) for _ in range(num)]

def gen_full_data(language_num, user_num, sentence_num):
    '''
    Generates a full dataset with languages, users and sentences
    '''
    users = create_random_users(user_num)
