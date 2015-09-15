'''
Public lang views
'''
from atcatalog import app
from flask import render_template


@app.route('/')
@app.route('/langs/')
def show_langs():
    ''' Show the languages the user owns and can change
    '''
    return render_template('index.html')


@app.route('/lang/<int:lid>/')
@app.route('/lang/<int:lid>/texts/')
def show_lang(lid):
    '''
    Show the content of the user language
    '''
    return render_template('publang.html', lid=lid)
