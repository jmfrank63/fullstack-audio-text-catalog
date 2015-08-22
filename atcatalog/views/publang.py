'''
Public language views
'''
from atcatalog import app


@app.route('/')
@app.route('/languages/')
def show_languages():
    '''
    Show the languages the user owns and can change
    '''
    return "Here all languages are shown"


@app.route('/language/<int:language_id>/')
@app.route('/language/<int:language_id>/texts/')
def show_language(language_id):
    '''
    Show the content of the user language
    '''
    return "Here the content of language with id {0} is shown".\
        format(language_id)
