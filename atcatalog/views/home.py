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
def home():
    ''' Show the welcome page
    '''
    languages = Language.query.all()
    return render_template('home.html', languages=languages)

@app.route('/mock_login')
def mock_login():
    ''' Show the login page
    '''
    users = User.query.all()
    return render_template('mock_login.html', users=users)

