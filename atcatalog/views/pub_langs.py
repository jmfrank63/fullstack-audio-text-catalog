'''
Public lang views
'''
from atcatalog import app
#from atcatalog.views.users import login
from flask import render_template, url_for

languages = {0: 'english', 1: 'spanish', 2: 'french', 3: 'german',
                 4: 'portuguese'}

@app.route('/')
@app.route('/langs/')
def pub_langs():
    ''' Show all public languages
    Link to the user login and the content of each language
    '''
    login_link = url_for('login')
    return render_template('pubLangs.html', langs=languages, login=login_link)


@app.route('/lang/<int:lid>/')
@app.route('/lang/<int:lid>/texts/')
def pub_lang(lid):
    '''
    Show the content of the public language with id = lid
    '''
    return render_template('pubLang.html', lid=lid)
