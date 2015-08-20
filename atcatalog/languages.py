from flask import redirect, url_for
from atcatalog import app


@app.route('/')
def index():
    '''
    This is the main page for all public visible languages.
    The page does not take any parameters.
    '''
    return "Here a list of all languages will be shown"


@app.route('/languages/')
def languages():
    '''
    This route just redirects to the main route
    '''
    return redirect(url_for('index'))


@app.route('/langauge/')
def language():
    '''
    This function redirects back to the main languages page
    since no language id has been given
    '''
    return redirect(url_for('languages'))


@app.route('/language/<int:language_id>/')
def langauge_id(language_id):
    '''
    This page shows the content of a public visible language
    with id <language_id>
    '''
    return "Here a list of all texts of language with id {0}"\
        " will be shown".format(language_id)
