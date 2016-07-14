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
import os
import cPickle as pickle
from atcatalog.data.const import *
from atcatalog.model.atcmodel import *


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
        self._sentences = value

    @force_encoded_string_output
    def __repr__(self):
        '''
        Pretty print of the object
        '''
        return u"<User:\n    name='{}',\n\
    email='{}',\n\
    codes='{}',\n\
    picture='{}',\n\
    sentences='{}'\n>".format(self.name,
                            self.email,
                            self.codes,
                            self.picture,
                            repr(self._sentences).decode('utf-8'))


class GenSentence(Sentence):
    '''
    Generated sentence works without the database
    '''
    def __init__(self, text, translation, audio,
                 code):
        super(GenSentence, self).__init__(text, translation, audio,
                                          1, 1)
        self.code = code

    @force_encoded_string_output
    def __repr__(self):
        '''
        Pretty print of the object
        '''
        return u"\n<Sentence:\n    text='{}',\n\
    translation='{}',\n\
    audio='{}',\n\
    code='{}',\n'>\n".format(self.text,
                           self.translation,
                           self.audio,
                           self.code)

# The language section *******
def create_random_code():
    '''
    Returns a random language code
    '''
    return random.choice(list(LANG_DICT.keys()))

def create_random_codes(num):
    '''
    Creates a list of language codes in random order
    '''
    codes = list(LANG_DICT.keys())
    random.shuffle(codes)
    if num >= len(codes):
        return codes
    return codes[:num]

def create_all_codes():
    '''
    Creates all languages
    '''
    return [GenLanguage(code) for code in LANG_DICT.keys()]

    # The users section **********
def create_random_user(codes):
    '''
    Creates a random user
    '''
    fake = faker.Factory.create(codes[0])
    name = fake.name()
    email = fake.email()
    picture = IMAGE
    user = GenUser(name, email, codes, picture)
    return user

# The sentence section ********
def create_random_sentence(code):
    '''
    Generates a random sentence of a given user and language code
    If language code is not given the first language code of the user
    is used.
    '''
    fake = faker.Factory.create(code)
    text = fake.sentence()
    translation = fake.sentence()
    audio = AUDIO_DUMMY
    sentence = GenSentence(text, translation, audio, code)
    return sentence


def gen_full_data(codes, user_num, sentence_num):
    '''
    Generates a full dataset with languages, users and sentences
    '''
    for _ in xrange(random.randint(1,user_num)):
        user = create_random_user(codes)
        for code in codes:
            user.sentences.extend([create_random_sentence(code)
                              for _ in xrange(sentence_num)])
        yield user

def create_gen_data(lang_num, user_num, sentence_num):
    '''
    Generates a data set and serializes it
    '''
    PFILE = DATA_PATH + PICKLE_FILE
    if not os.path.exists(PFILE):
        with open(PFILE, 'wb') as pfile:
            for _ in xrange(lang_num):
                codes = create_random_codes(lang_num)
                for user in gen_full_data(codes, user_num, sentence_num):
                    pickle.dump(user, pfile, pickle.HIGHEST_PROTOCOL)
    return get_gen_data(lang_num, user_num, sentence_num)

def get_gen_data(lang_num, user_num, sentence_num):
    '''
    Reads a previously saved dataset
    '''
    PFILE = DATA_PATH + PICKLE_FILE
    gen_data = []
    if os.path.exists(PFILE):
        with open(PFILE, 'rb') as pfile:
            try:
                while(True):
                    gen_data.append(pickle.load(pfile))
            except EOFError:
                pass
        return gen_data
    return create_gen_data(lang_num, user_num, sentence_num)

def read_csv(fname):
    '''
    reads the content of a csv file and
    returns its results as a generator
    '''
    with open(DATA_PATH + fname, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # we skip the header
        reader.next()
        return [row for row in reader]

if __name__ == '__main__':
    users = gen_full_data(LANG_NUM, USER_NUM, SENTENCE_NUM)
    print(users)