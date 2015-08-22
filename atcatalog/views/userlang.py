'''
User language views
'''
from atcatalog import app


@app.route('/user/<int:user_id>/')
@app.route('/user/<int:user_id>/languages/')
def show_user_languages(user_id):
    '''
    Show the languages the user owns and can change
    '''
    return "Here the user with id  {0} sees his own languages".format(user_id)


@app.route('/user/<int:user_id>/language/<int:language_id>/')
@app.route('/user/<int:user_id>/language/<int:language_id>/texts/')
def show_user_language(user_id, language_id):
    '''
    Show the content of the user language
    '''
    return "Here the user's {0} content of language with id {1} is shown".\
        format(user_id, language_id)


@app.route('/user/<int:user_id>/language/add/')
def add_user_language(user_id):
    '''
    This page lets the user add a language
    '''
    return "Here the user {0} can add a language".format(user_id)


@app.route('/user/<int:user_id>/language/<int:language_id>/edit/')
def edit_user_language(user_id, language_id):
    '''
    This page lets the user edit a language
    '''
    return "Here the user {0} can edit a language with id {1}"\
        .format(user_id, language_id)


@app.route('/user/<int:user_id>/language/<int:language_id>/delete/')
def delete_user_language(user_id, language_id):
    '''
    This page lets the user delete a language
    '''
    return "Here user {0} can delete a language"
