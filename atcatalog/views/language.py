# -*- coding: utf-8 -*-
'''
Public language view
'''
from atcatalog import app
from flask import render_template, url_for
from atcatalog.model.atcmodel import db, Language, User, Sentence

@app.route('/language/<int:lid>/')
def show_language(lid):
    '''
    Show the content of the public language with id = lid
    '''
    language = Language.query.get(lid)
    sentences = Sentence.query.filter_by(language_id=lid)
    return render_template('show_language.html',
                            language=language,
                            sentences=sentences)
