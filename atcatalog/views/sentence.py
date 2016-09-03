# -*- coding: utf-8 -*-
'''
Public text views
'''
from atcatalog import app
from flask import render_template
from atcatalog.model.atcmodel import *

@app.route('/language/<int:lid>/sentence/<int:sid>/')
def show_sentence(lid, sid):
    '''
    Show sentence text with translation and audio
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('show_sentence.html', sentence=sentence)


@app.route('/language/<int:lid>/sentence/<int:sid>/text/')
def show_sentence_text(lid, sid):
    '''
    Show sentence text
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('show_sentence_text.html', sentence=sentence)


@app.route('/language/<int:lid>/sentence/<int:sid>/translation/')
def show_sentence_translation(lid, sid):
    '''
    Show sentence translation
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('show_sentence_translation.html', sentence=sentence)


@app.route('/language/<int:lid>/sentence/<int:sid>/audio/')
def show_sentence_audio(lid, sid):
    '''
    Show sentence audio
    '''
    sentence = Sentence.query.filter_by(language_id=lid, id=sid).one()
    return render_template('show_sentence_audio.html', sentence=sentence)
