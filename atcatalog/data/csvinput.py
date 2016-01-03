'''
Reads content from csv formated files to fill the database
'''
from atcatalog import app
from atcatalog.data import dbfill
from atcatalog.data.dbsetup import User, Language, Sentence
import csv
import os

def read_users():
    '''
    reads the content of user.csv into the orm
    '''
    

