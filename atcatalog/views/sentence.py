# coding=utf-8
'''
Public text views
'''
from atcatalog import app
from flask import render_template
from atcatalog.data.fake import languages, sentences

@app.route('/language/<int:lid>/sentence/<int:sid>/')
def show_sentence(lid, sid):
    '''
    Show sentence text with translation and audio
    '''
    return render_template('show_sentence.html', lid=lid, sid=sid, 
                            sentence=sentences[lid][sid])


@app.route('/language/<int:lid>/sentence/<int:sid>/text/')
def show_sentence_text(lid, sid):
    '''
    Show sentence text
    '''
    return render_template('show_sentence_text.html', lid=lid, sid=sid,
                            sentence=sentences[lid][sid])


@app.route('/language/<int:lid>/sentence/<int:sid>/translation/')
def show_sentence_translation(lid, sid):
    '''
    Show sentence translation
    '''
    return render_template('show_sentence_translation.html', lid=lid, sid=sid,
                            sentence=sentences[lid][sid])


@app.route('/language/<int:lid>/sentence/<int:sid>/audio/')
def show_sentence_audio(lid, sid):
    '''
    Show sentence audio
    '''
    return render_template('show_sentence_audio.html', lid=lid, sid=sid,
                            sentence=sentences[lid][sid])
