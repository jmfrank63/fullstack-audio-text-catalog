'''
Public languages views
'''
from atcatalog import app
from flask import render_template, url_for
from atcatalog.langdata.langdicts import language


@app.route('/')
@app.route('/langs/')
def pub_langs():
    ''' Show all public language
    Link to the user login and the content of each language
    '''
    login_link = url_for('login')
    return render_template('publangs.html', langs=language, login=login_link)


@app.route('/lang/<int:lid>/')
@app.route('/lang/<int:lid>/sents/')
def pub_lang(lid):
    '''
    Show the content of the public language with id = lid
    '''
    return render_template('publang.html', lid=lid)
