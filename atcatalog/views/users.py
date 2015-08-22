'''
User module only for import
'''
from atcatalog import app


@app.route('/login/')
def login():
    '''
    This site is the login site were users can chose the login type
    '''
    return "Here the user can login"


@app.route('/logout/<int:user_id>/')
def logout(user_id):
    '''
    This site is the logout site were users are confirmed to logout
    '''
    return "Here the user with id {0} can logout ".format(user_id)
