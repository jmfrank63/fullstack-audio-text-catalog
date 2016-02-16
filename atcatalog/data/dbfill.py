# -*- coding: utf-8 -*-
'''
This module provides helper functions filling the database with entries
'''
from atcatalog.model.atcmodel import *
from atcatalog.data.gendata import *
from atcatalog.data.const import *



if __name__ == '__main__':
    make_db()
    languages, users, sentences = create_gen_data(LANG_NUM, USER_NUM, SENTENCE_NUM)
    db.session.add_all(languages)
    for user in users:
        db.session.add(user)
        db.session.flush()
