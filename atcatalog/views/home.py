# -*- coding: utf-8 -*-
'''
The starting page
'''
from atcatalog import app, login_manager
from atcatalog.model.atcmodel import User, Language, Sentence
from flask_breadcrumbs import register_breadcrumb
from flask_login import current_user
from flask import render_template, url_for, request


@app.route('/')
@register_breadcrumb(app, '.', 'Home')
def home():
    ''' Show the home page with public languages
    '''
    languages = Language.query.all()
    if current_user.is_authenticated:
        user_languages = Language.query.filter(Language.code.in_(current_user.codes)).all()
    else:
        user_languages = None
    return render_template('home.html',
                            languages=languages,
                            user_languages=user_languages)

@app.route('/mock_login')
def mock_login():
    ''' A page showing all users for testing
    '''
    users = User.query.all()
    return render_template('mock_login.html', users=users)
