# -*- coding: utf-8 -*-
'''
Public language view
'''
from atcatalog import app
from flask.ext.breadcrumbs import register_breadcrumb
from flask import render_template, url_for, request
from atcatalog.model.atcmodel import db, Language, User, Sentence

def view_language(*args, **kwargs):
    ''' Construct a language name for breadcrumbs
    '''
    lid = request.view_args['lid']
    language = Language.query.get(lid)
    return [{'text' : u"Language {}".format(language.name),
             'url' : u"/language/{}/".format(lid)}]

@app.route('/language/<int:lid>/')
@register_breadcrumb(app, '.language', 'Language', dynamic_list_constructor=view_language)
def language(lid):
    '''
    Show the content of the public language with id = lid
    '''
    language = Language.query.get(lid)
    sentences = Sentence.query.filter_by(language_id=lid)
    return render_template('language.html',
                            language=language,
                            sentences=sentences)