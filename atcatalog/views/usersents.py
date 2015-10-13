'''
User text views
'''
from atcatalog import app


@app.route('/user/<int:uid>/lang/<int:lid>/text/add/')
def add_user_text(uid, lid):
    ''' Lets the user add a text to his langauge
    '''
    return "Here the user {0} can add a text to language {1}"\
        .format(uid, lid)


@app.route('/user/<int:uid>/lang/<int:lid>/text/<int:tid>/edit/')
def edit_user_text(uid, lid, tid):
    ''' Lets the user edit a text of his langauge
    '''
    return "Here the user {0} can edit a text with id {2} of language {1}"\
        .format(uid, lid, tid)


@app.route('/user/<int:uid>/lang/<int:lid>/text/<int:tid>/del/')
def del_user_text(uid, lid, tid):
    ''' Lets the user delete a text of his langauge
    '''
    return "Here the user {0} can delete a text with id {2} of language {1}"\
        .format(uid, lid, tid)


@app.route('/user/<int:uid>/lang/<int:lid>/text/<int:tid>/')
@app.route('/user/<int:uid>/lang/<int:lid>/text/<int:tid>/both/')
def show_user_text_both(uid, lid, tid):
    ''' Shows the writing part of the text
    '''
    return "Here the user {0} can show the text {2} writing and audio part \
        of language {1}".format(uid, lid, tid)


@app.route('/user/<int:uid>/lang/<int:lid>/text/<int:tid>/writing/')
def show_user_text_writing(uid, lid, tid):
    ''' Shows the writing part of the text
    '''
    return "Here the user {0} can show the text {2} writing part \
        of language {1}".format(uid, lid, tid)


@app.route('/user/<int:uid>/lang/<int:lid>/text/<int:tid>/audio/')
def show_user_text_audio(uid, lid, tid):
    ''' Shows the audio part of the text
    '''
    return "Here the user {0} can show the text {2} audio part \
    of lang {1}".format(uid, lid, tid)
