'''
Public text views
'''
from atcatalog import app


@app.route('/lang/<int:lid>/text/<int:tid>/')
def show_text_index(lid, tid):
    '''
    Show text writing and audio
    '''
    return "Here the text's {1} audio and writing of language {0} are shown"\
        .format(lid, tid)


@app.route('/lang/<int:lid>/text/<int:tid>/both/')
def show_text_both(lid, tid):
    '''
    Show text writing and audio
    '''
    return "Here the text's {1} audio and writing of language {0} are shown"\
        .format(lid, tid)


@app.route('/lang/<int:lid>/text/<int:tid>/writing/')
def show_text_writing(lid, tid):
    '''
    Show text writing
    '''
    return "Here the text's {1} writing of language {0} are shown"\
        .format(lid, tid)


@app.route('/lang/<int:lid>/text/<int:tid>/audio/')
def show_text_audio(lid, tid):
    '''
    Show text audio
    '''
    return "Here the text's {1} audio of language {0} are shown"\
        .format(lid, tid)
