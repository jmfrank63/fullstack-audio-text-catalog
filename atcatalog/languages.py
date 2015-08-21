'''
Language and text views
'''
from flask import redirect, url_for
from atcatalog import app


@app.route('/')
@app.route('/languages/')
def index():
    '''
    This is the main page for all public visible languages.
    The page does not take any parameters.
    '''
    return "Here a list of all languages will be shown"


@app.route('/language/<int:language_id>/')
@app.route('/language/<int:language_id>/texts')
def langauge_id(language_id):
    '''
    This page shows the content of a public visible language
    with id <language_id>
    '''
    return "Here a list of all texts of language with id {0}"\
        " will be shown".format(language_id)
