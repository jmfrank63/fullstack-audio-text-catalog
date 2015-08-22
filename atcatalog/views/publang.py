'''
Public lang views
'''
from atcatalog import app


@app.route('/')
@app.route('/langs/')
def show_langs():
    ''' Show the languages the user owns and can change
    '''
    return "Here all languages are shown"


@app.route('/lang/<int:lid>/')
@app.route('/lang/<int:lid>/texts/')
def show_lang(lid):
    '''
    Show the content of the user language
    '''
    return "Here the content of language with id {0} is shown".\
        format(lid)
