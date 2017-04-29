# -*- coding: utf-8 -*-
'''
The starting page
'''
from atcatalog import app,login_manager
from atcatalog.model.atcmodel import User, Language, Sentence
from flask_login import login_required, login_user, current_user, logout_user
from flask_breadcrumbs import register_breadcrumb
from flask import render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from sqlalchemy.orm.exc import NoResultFound

@login_manager.user_loader
def load_user(uid):
    '''
    Get a user object by unicode user id
    '''
    return User.query.get(int(uid))

def view_user_languages(*args, **kwargs):
    ''' Construct a user name for breadcrumbs
    '''
    uid = request.view_args['uid']
    user = User.query.get(uid)
    return [{'text' : u"{}".format(user.name),
             'url' : "/user/{}/".format(uid)}]

class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
@register_breadcrumb(app, '.login', 'Login')
def login():
    ''' Show the login page
    '''
    login_form=LoginForm()
    if login_form.validate_on_submit():
        email = request.form['email']
        try:
            user = User.query.filter_by(email=email).one()
            login_user(user)
            return redirect(url_for('user_languages', uid=user.id))
        except NoResultFound:
            user = None
        return redirect(url_for('login'))
    return render_template('login.html', form=login_form)

@app.route('/user/<int:uid>/')
@login_required
@register_breadcrumb(app, '.user', 'User', dynamic_list_constructor=view_user_languages)
def user_languages(uid):
    ''' Show the user page
    '''
    if current_user.id == uid:
        user = User.query.get(uid)
        languages = Language.query.filter(Language.code.in_(user.codes)).all()
        return render_template('user_languages.html', user=user,languages=languages)
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    '''
    Logouts the user
    '''
    logout_user()
    return(redirect(url_for('home')))

