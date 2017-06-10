# -*- coding: utf-8 -*-
'''
Public text views
'''
from atcatalog import app
from atcatalog.views.users import user_required
from atcatalog.model.atcmodel import Language, User, Sentence
from flask import render_template, request, redirect, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_wtf import FlaskForm
from sqlalchemy.orm.exc import NoResultFound
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


# Public languages
# ----------------
def view_sentence(*args, **kwargs):
    ''' Construct the sentence name for breadcrumbs
    '''
    lid = request.view_args['lid']
    sid = request.view_args['sid']
    sentence = Sentence.query.filter_by(language_id=lid,
                                        id=sid).one()
    return [{'text' : u"Sentence {}".format(sentence.id),
             'url' : '/language/{}/sentence/{}/'.format(lid, sid) }]

@app.route('/language/<int:lid>/sentence/<int:sid>/')
@register_breadcrumb(app, '.language.sentence', 'Sentence', dynamic_list_constructor=view_sentence)
def sentence(lid, sid):
    '''
    Show sentence text with translation and audio
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('sentence.html', sentence=sentence)

@app.route('/language/<int:lid>/sentence/<int:sid>/text/')
@register_breadcrumb(app, '.language.sentence.text', 'Text')
def sentence_text(lid, sid):
    '''
    Show sentence text
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('sentence_text.html', sentence=sentence)


@app.route('/language/<int:lid>/sentence/<int:sid>/translation/')
@register_breadcrumb(app, '.language.sentence.translation', 'Translation')
def sentence_translation(lid, sid):
    '''
    Show sentence translation
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('sentence_translation.html', sentence=sentence)


@app.route('/language/<int:lid>/sentence/<int:sid>/audio/')
@register_breadcrumb(app, '.language.sentence.audio', 'Audio')
def sentence_audio(lid, sid):
    '''
    Show sentence audio
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('sentence_audio.html', sentence=sentence)

# User Sentence
# -------------
def view_user_sentence(*args, **kwargs):
    ''' Construct the sentence name for breadcrumbs
    '''
    uid = request.view_args['uid']
    lid = request.view_args['lid']
    sid = request.view_args['sid']
    sentence = Sentence.query.filter_by(user_id=uid,
                                        language_id=lid,
                                        id=sid).one()
    return [{'text' : u"Sentence {}".format(sentence.id),
             'url' : '/user/{}/language/{}/sentence/{}/'
             .format(uid, lid, sid) }]

@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/')
@user_required
@register_breadcrumb(app, '.user.language.sentence', 'Sentence',
                     dynamic_list_constructor=view_user_sentence)
def user_sentence(uid, lid, sid):
    '''
    Show user sentence text with translation and audio
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence.html', sentence=sentence)

@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/text/')
@user_required
@register_breadcrumb(app, '.user.language.sentence.text', 'Text')
def user_sentence_text(uid, lid, sid):
    '''
    Show user sentence text
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence_text.html', sentence=sentence)


@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/translation/')
@user_required
@register_breadcrumb(app, '.user.language.sentence.translation', 'Translation')
def user_sentence_translation(uid, lid, sid):
    '''
    Show user sentence translation
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence_translation.html', sentence=sentence)


@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/audio/')
@user_required
@register_breadcrumb(app, '.user.language.sentence.audio', 'Audio')
def user_sentence_audio(uid, lid, sid):
    '''
    Show user sentence audio
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence_audio.html', sentence=sentence)

# Edit User Sentence
# ------------------
def view_edit_sentence(*args, **kwargs):
    ''' Construct the sentence name for breadcrumbs
    '''
    uid = request.view_args['uid']
    lid = request.view_args['lid']
    sid = request.view_args['sid']
    sentence = Sentence.query.filter_by(user_id=uid,
                                        language_id=lid,
                                        id=sid).one()
    return [{'text' : u"Edit Sentence {}".format(sentence.id),
             'url' : '/user/{}/language/{}/sentence/{}/'
             .format(uid, lid, sid) }]

class SentenceEditForm(FlaskForm):
    '''
    Get the new sentence name
    '''
    text = StringField('Text', validators=[DataRequired()])
    translation = StringField('Translation', validators=[DataRequired()])
    audio = StringField('Audio', validators=[DataRequired()])

@app.route('/user/<int:uid>/language/<int:lid>/edit_sentence/<int:sid>/')
@user_required
@register_breadcrumb(app, '.user.language.edit_sentence', 'Edit Sentence',
                     dynamic_list_constructor=view_edit_sentence)
def edit_sentence(uid, lid, sid):
    '''
    Edit the user sentence
    '''
    user = User.query.get(uid)
    language = Language.query.get(lid)
    if user is None or language not in user.languages:
        return redirect(url_for('home'))
    try:
        sentence = Sentence.query.filter_by(user_id=uid,
                                            language_id=lid,
                                            id=sid).one()
    except NoResultFound:
        return redirect(url_for('home'))

    if User is None or language not in user.languages \
    or sentence not in user.sentences:
        return redirect(url_for('home'))
    sentence_edit_form = SentenceEditForm(text=sentence.text,
                                          translation=sentence.translation,
                                          audio=sentence.audio)
    if sentence_edit_form.validate_on_submit():
        text = request.form['text']
        sentence.text = text
        sentence.translation = translation
        sentence.audio = audio
        db.session.add(sentence)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_sentence.html', form=sentence_edit_form,
                                                 user=user,
                                                 language=language,
                                                 sentence=sentence)