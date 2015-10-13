'''
Public languages views
'''
from atcatalog import app
from flask import render_template, url_for
from atcatalog.langdata.lang_dicts import languages


@app.route('/')
@app.route('/langs/')
def pub_langs():
    ''' Show all public languages
    Link to the user login and the content of each language
    '''
    login_link = url_for('login')
    return render_template('pub_langs.html', langs=languages, login=login_link)


@app.route('/lang/<int:lid>/')
@app.route('/lang/<int:lid>/sents/')
def pub_lang(lid):
    '''
    Show the content of the public language with id = lid
    '''
    return render_template('pub_lang.html', lid=lid)
