'''
Main project flask file for the audio text catalog
'''
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from os import getenv

import users

app = Flask(__name__)

@app.route('/')
@app.route('/languages/')
def languages():
    '''
    This is the main page for all public visible languages.
    The page does not take any parameters.
    '''
    return "Here a list of all languages will be shown"

@app.route('/language/<int:language_id>/')
def langauge(language_id):
    '''
    This page shows the content of a public visible language
    with id <language_id>
    '''
    return "Here a list of all texts of language with id {0}"\
            " will be shown".format(language_id)


if __name__ == '__main__':
    app.secret_key = 'udacity_secret_app_development_key'
    app.debug = True
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=getenv('IP','0.0.0.0'), port=int(getenv('PORT', '8080')))
