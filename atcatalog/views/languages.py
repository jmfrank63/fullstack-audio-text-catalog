# -*- coding: utf-8 -*-
'''
Public languages views
'''
from atcatalog import app
from flask import render_template, url_for
from atcatalog.model.atcmodel import Language


@app.route('/')
def languages():
    ''' Show all public language
    '''
    languages = Language.query.all()
    return render_template('languages.html', 
                           languages=languages)
