# -*- coding: utf-8 -*-
'''
Public text views
'''
from atcatalog import app
from flask.ext.breadcrumbs import register_breadcrumb
from flask import render_template, request
from atcatalog.model.atcmodel import *

def view_sentence(*args, **kwargs):
    ''' Construct the sentence name for breadcrumbs
    '''
    lid = request.view_args['lid']
    sid = request.view_args['sid']
    sentence = Sentence.query.filter_by(language_id=lid,
                                        id=sid).one()
    return [{'text' : u"Sentence {}".format(sentence.id),
             'url' : '/language/{}/sentence/{}/'.format(lid, sid) }]

# Public languages
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

# User language and sentences
@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/')
@register_breadcrumb(app, '.user.language.sentence', 'Sentence', dynamic_list_constructor=view_sentence)
def user_sentence(uid, lid, sid):
    '''
    Show user sentence text with translation and audio
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence.html', sentence=sentence)

@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/text/')
@register_breadcrumb(app, '.user.language.sentence.text', 'Text')
def user_sentence_text(uid, lid, sid):
    '''
    Show user sentence text
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence_text.html', sentence=sentence)


@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/translation/')
@register_breadcrumb(app, '.user.language.sentence.translation', 'Translation')
def user_sentence_translation(uid, lid, sid):
    '''
    Show user sentence translation
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence_translation.html', sentence=sentence)


@app.route('/user/<int:uid>/language/<int:lid>/sentence/<int:sid>/audio/')
@register_breadcrumb(app, '.user.language.sentence.audio', 'Audio')
def user_sentence_audio(uid, lid, sid):
    '''
    Show user sentence audio
    '''
    sentence = Sentence.query.filter_by(user_id=uid, language_id=lid, id=sid).one()
    return render_template('user_sentence_audio.html', sentence=sentence)
