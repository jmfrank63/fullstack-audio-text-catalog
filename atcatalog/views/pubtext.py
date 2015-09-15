'''
Public text views
'''
from atcatalog import app
from flask import render_template

@app.route('/lang/<int:lid>/text/<int:tid>/')
@app.route('/lang/<int:lid>/text/<int:tid>/both/')
def show_text_both(lid, tid):
    '''
    Show text writing and audio
    '''
    return render_template('show_text_both.html', lid=lid, tid=tid)


@app.route('/lang/<int:lid>/text/<int:tid>/writing/')
def show_text_writing(lid, tid):
    '''
    Show text writing
    '''
    return render_template('show_text_writing.html', lid=lid, tid=tid)


@app.route('/lang/<int:lid>/text/<int:tid>/audio/')
def show_text_audio(lid, tid):
    '''
    Show text audio
    '''
    return render_template('show_text_audio.hmtl', lid=lid, tid=tid)
