# -*- coding: utf-8 -*-
'''
The starting page
'''
from atcatalog import app,login_manager
from atcatalog.model.atcmodel import User, Language, Sentence
from flask_login import login_required, login_user, current_user, logout_user
from flask_breadcrumbs import register_breadcrumb
from flask import render_template, url_for, request, redirect, Response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from sqlalchemy.orm.exc import NoResultFound
from urlparse import urlparse, urljoin
from functools import wraps

@login_manager.user_loader
def load_user(uid):
    '''
    Get a user object by unicode user id
    '''
    return User.query.get(int(uid))

# @login_required is not suitable as different
# pages are dependent on the user id
# Therefore we write our own decorator
# Used http://stackoverflow.com/questions/19376165/flask-pluggable-views-and-login-required
def user_required(func):
    '''
    Check for correct user id in additon to authenticated
    '''
    @wraps(func)
    def decorated(*args, **kwargs):
        uid = kwargs['uid']
        if current_user.is_authenticated and current_user.id == uid:
            func(*args, **kwargs)
            return func(*args, **kwargs)
        return login_manager.unauthorized()
    return decorated


def view_user_languages(*args, **kwargs):
    ''' Construct a user name for breadcrumbs
    '''
    uid = request.view_args['uid']
    user = User.query.get(uid)
    return [{'text' : u"{}".format(user.name),
             'url' : "/user/{}/".format(uid)}]

# Taken from http://flask.pocoo.org/snippets/62/
def is_safe_url(target):
    '''
    Check if url points to the same server
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

def get_uid_from_url(url):
    '''
    Get the uid from the url
    '''
    if url is None:
        return None
    url_list = url.split('/')
    try:
        user_pos = url_list.index('user')
        return int(url_list[url_list.index('user') + 1])
    except ValueError:
        return None

class LoginForm(FlaskForm):
    '''
    Get the user email for login
    '''
    email = StringField('E-Mail', validators=[DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
@register_breadcrumb(app, '.login', 'Login')
def login():
    ''' Show the login page
    '''
    if current_user.is_authenticated:
        return redirect(url_for('logout'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = request.form['email']
        try:
            user = User.query.filter_by(email=email).one()
            login_user(user)
            return redirect(url_for('user_languages', uid=user.id))
        except NoResultFound:
            return redirect(url_for('login'))
    return render_template('login.html', form=login_form)

@app.route('/user/<int:uid>/')
@user_required
@register_breadcrumb(app, '.user', 'User', dynamic_list_constructor=view_user_languages)
def user_languages(uid):
    ''' Show the user page with languages and edit options
    '''
    user = User.query.get(uid)
    languages = Language.query.filter(Language.code.in_(user.codes)).all()
    return render_template('user_languages.html', user=user,languages=languages)

@app.route('/logout')
@login_required
def logout():
    '''
    Logouts the user
    '''
    logout_user()
    return redirect(url_for('home'))

