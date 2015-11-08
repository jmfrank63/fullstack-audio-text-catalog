# coding=utf-8
'''
Public language view
'''
from atcatalog import app
from flask import render_template, url_for
from atcatalog.data.fake import languages, sentences

@app.route('/language/<int:lid>/')
def show_language(lid):
    '''
    Show the content of the public language with id = lid
    '''
    return render_template('language.html', lid=lid, lang_name=languages[lid],
                            sentences=sentences[lid])
