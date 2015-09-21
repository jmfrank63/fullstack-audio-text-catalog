'''
Public lang views
'''
from atcatalog import app
from flask import render_template


@app.route('/')
@app.route('/langs/')
def show_pub_langs():
    ''' Show all public languages
    '''
    return render_template('pubLangs.html')


@app.route('/lang/<int:lid>/')
@app.route('/lang/<int:lid>/texts/')
def show_pub_lang(lid):
    '''
    Show the content of the public language with id = lid
    '''
    return render_template('pubLang.html', lid=lid)
