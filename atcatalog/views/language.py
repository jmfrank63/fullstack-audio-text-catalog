# -*- coding: utf-8 -*-
'''
Public language view
'''
from atcatalog import app
from atcatalog.views.users import user_required
from atcatalog.model.atcmodel import db, Language, User, Sentence
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required
from flask import render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from sqlalchemy.orm.exc import NoResultFound
from sqlite3 import IntegrityError
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError


# Public language
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

# User language
def view_user_language(*args, **kwargs):
    ''' Construct a language name for breadcrumbs
    '''
    uid = request.view_args['uid']
    lid = request.view_args['lid']
    language = Language.query.get(lid)
    return [{'text' : u"{}".format(language.name),
             'url' : u"/user/{}/language/{}/".format(uid, lid)}]

@app.route('/user/<int:uid>/language/<int:lid>/')
@user_required
@register_breadcrumb(app, '.user.language', 'Language',
                     dynamic_list_constructor=view_user_language)
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

def view_edit_language(*args, **kwargs):
    ''' Construct a language name for breadcrumbs
    '''
    lid = request.view_args['lid']
    language = Language.query.get(lid)
    return [{'text' : u"edit {}".format(language.name),
             'url' : u"/edit_language/{}/".format(lid)}]

class LanguageEditForm(FlaskForm):
    '''
    Get the new language name
    '''
    name = StringField('Name', validators=[DataRequired()])

@app.route('/user/<int:uid>/edit_language/<int:lid>/', methods=['GET', 'POST'])
@user_required
@register_breadcrumb(app, '.edit_language', 'Edit Language',
                     dynamic_list_constructor=view_edit_language)
def edit_language(uid, lid):
    '''
    Edit the language name
    Until admin access is added all users are allowed to edit their own lanugage names
    '''
    user = User.query.get(uid)
    language = Language.query.get(lid)
    if language not in user.languages:
        return(redirect(url_for('home')))
    language_edit_form = LanguageEditForm(name=language.name)
    if language_edit_form.validate_on_submit():
        name = request.form['name']
        language.name = name
        db.session.add(language)
        db.session.commit()
        return(redirect(url_for('home')))
    return render_template('edit_language.html',
                            form=language_edit_form,
                            user=user,
                            language=language)

class LanguageAddForm(FlaskForm):
    '''
    Get the new language name
    '''
    code = StringField('Code', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])

    def validate_code(form, field):
        '''
        Check if name already exists in database
        '''
        language_details = LanguageDetails.query.filter_by(code=field.data).first()
        if language_details:
            raise ValidationError

    def validate_name(form, field):
        '''
        Check if name already exists in database
        '''
        language = Language.query.filter_by(name=field.data).first()
        if language:
            raise ValidationError

@app.route('/user/<int:uid>/add_language/', methods=['GET', 'POST'])
@user_required
@register_breadcrumb(app, '.add_language', 'Add Language')
def add_language(uid):
    '''
    Add a language name
    '''
    user = User.query.get(uid)
    language_add_form = LanguageAddForm()
    if language_add_form.validate_on_submit():
        code = request.form['code']
        name = request.form['name']
        lang_details = LanguageDetails(code=code,name=name)
        language = Language(name)
        db.session.add(language)
        db.session.commit()
        return(redirect(url_for('home')))
    return render_template('add_language.html',
                            form=language_add_form,
                            user=user)