# -*- coding: utf-8 -*-
'''
Public languages views
'''
from atcatalog import app
from flask import render_template, url_for
from atcatalog.data.fake import LANGUAGES


@app.route('/')
def show_languages():
    ''' Show all public language
    '''
    return render_template('show_languages.html', languages=LANGUAGES)


