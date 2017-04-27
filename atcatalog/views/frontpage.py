# -*- coding: utf-8 -*-
'''
The starting page
'''
from atcatalog import app, login_manager
from flask.ext.breadcrumbs import register_breadcrumb
from flask import render_template, url_for, request
from atcatalog.model.atcmodel import User, Language, Sentence

@app.route('/')
@register_breadcrumb(app, '.', 'Home')
def frontpage():
    ''' Show the welcome page
    '''
    languages = Language.query.all()
    return render_template('frontpage.html', languages=languages)

@app.route('/login')
@register_breadcrumb(app, '.login', 'Login')
def login():
    ''' Show the login page
    '''
    return render_template('login.html', return_page=url_for('frontpage'))

def view_userpage(*args, **kwargs):
    ''' Construct a user name for breadcrumbs
    '''
    user_id = request.view_args['uid']
    user = User.query.get(user_id)
    return [{'text' : u"{}".format(user.name), 'url' : u""}]

@app.route('/user/<int:uid>/')
@register_breadcrumb(app, '.user', 'User', dynamic_list_constructor=view_userpage)
def userpage(uid):
    ''' Show the user page
    '''
    user = User.query.get(uid)
    languages = Language.query.filter(Language.code.in_(user.codes)).all()
    return render_template('userpage.html', user=user,languages=languages)

@app.route('/mock_login')
def mock_login():
    ''' Show the login page
    '''
    users = User.query.all()
    return render_template('mock_login.html', users=users)

def view_language(*args, **kwargs):
    ''' Construct a language name for breadcrumbs
    '''
    lang_id = request.view_args['lid']
    language = Language.query.get(lang_id)
    return [{'text' : u"{}".format(language.name), 'url' : u""}]

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