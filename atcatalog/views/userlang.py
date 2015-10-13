'''
User lang views
'''
from atcatalog import app


@app.route('/user/<int:uid>/')
@app.route('/user/<int:uid>/langs/')
def show_user_langs(uid):
    ''' Show the langs the user owns and can change
    '''
    return "Here the user with id  {0} sees his own langs".format(uid)


@app.route('/user/<int:uid>/lang/<int:lid>/')
@app.route('/user/<int:uid>/lang/<int:lid>/texts/')
def show_user_lang(uid, lid):
    ''' Show the content of the user lang
    '''
    return "Here the user's {0} content of lang with id {1} is shown".\
        format(uid, lid)


@app.route('/user/<int:uid>/lang/add/')
def add_user_lang(uid):
    ''' This page lets the user add a lang
    '''
    return "Here the user {0} can add a lang".format(uid)


@app.route('/user/<int:uid>/lang/<int:lid>/edit/')
def edit_user_lang(uid, lid):
    ''' This page lets the user edit a lang
    '''
    return "Here the user {0} can edit a lang with id {1}"\
        .format(uid, lid)


@app.route('/user/<int:uid>/lang/<int:lid>/del/')
def del_user_lang(uid, lid):
    ''' This page lets the user del a lang
    '''
    return "Here user {0} can del a lang"
