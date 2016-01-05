'''
Reads content from csv formated files to fill the database
'''
from atcatalog import app
from atcatalog.data.dbsetup import User, Language, Sentence
import atcatalog.data.const as const
import csv
import os


def read_csv(table):
    '''
    reads the content of a csv file and 
    returns its results as a generator
    '''
    with open(const.DATA_DIR + table, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # we skip the header
        reader.next()
        for row in reader:
            yield row

def read_languages():
    '''
    returns a generator of languages.csv
    '''
    return read_csv(const.LANGUAGE_FILE)

def read_users():
    '''
    returns a generator of user.csv
    '''
    return read_csv(const.USER_FILE)

def read_sentences():
    '''
    returns a generator of sentences.csv
    '''
    return read_csv(const.SENTENCE_FILE)

def read_all():
    '''
    read all files
    '''
    languages = read_languages()
    users = read_users()
    sentences = read_sentences()
    return languages, users, sentences

if __name__ == '__main__':
    read_all()

    