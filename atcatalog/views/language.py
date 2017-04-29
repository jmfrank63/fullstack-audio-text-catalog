# -*- coding: utf-8 -*-
'''
Public language view
'''
from atcatalog import app
from atcatalog.model.atcmodel import Language, User, Sentence
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required
from flask import render_template, url_for, request


def view_language(*args, **kwargs):
    ''' Construct a language name for breadcrumbs
    '''
    lid = request.view_args['lid']
    language = Language.query.get(lid)
    return [{'text' : u"{}".format(language.name),
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
                            
@app.route('/user/<int:uid>/language/<int:lid>')
@login_required
@register_breadcrumb(app, '.user.language', 'Language', dynamic_list_constructor=view_language)
def user_language(uid, lid):
    '''
    Show the content of the user language with id = lid
    Give access to modifying the content
    '''
    language = Language.query.get(lid)
    sentences = Sentence.query.filter_by(user_id=uid, language_id=lid)
    return render_template('user_language.html',
                            language=language,
                            sentences=sentences)
    