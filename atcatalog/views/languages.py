'''
Public languages views
'''
from atcatalog import app
from flask import render_template, url_for
from atcatalog.data.fake import languages


@app.route('/')
def show_languages():
    ''' Show all public language
    '''
    return render_template('languages.html', languages=languages)


