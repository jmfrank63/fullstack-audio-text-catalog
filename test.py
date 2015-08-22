'''
Testfile for testing flask functionallity
'''
from atcatalog import app
from random import randint
import unittest


class Test_status_routes(unittest.TestCase):
    '''
    Testing status codes of flask routes
    '''
    def test_status_index(self):
        ''' Test of status code of main '/' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_langs(self):
        ''' Test of status code of langs '/langs' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/langs/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_lang(self):
        ''' Test of status code of lang '/lang/<int:lid>'
        '''
        test_client = app.test_client(self)
        lid = randint(1, 100)
        response = test_client.get('/lang/{0}/'.format(lid),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_lang_texts(self):
        ''' Test of status code of lang '/lang/<int:lid>/texts'
        '''
        test_client = app.test_client(self)
        lid = randint(1, 100)
        response = test_client.get('/lang/{0}/texts/'.format(lid),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_index(self):
        ''' Test of status code of lang
        '/user/<int:uid>/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        response = test_client.get('/user/{0}/'.format(uid),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_langs(self):
        ''' Test of status code of lang
        '/user/<int:uid>/langs/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        response = test_client.get('/user/{0}/langs/'.format(uid),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_lang_texts(self):
        ''' Test of status code of lang
        '/user/<int:uid>/lang/<int:lid>/texts/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/texts/'.format(uid, lid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_lang_index(self):
        ''' Test of status code of lang
        '/user/<int:uid>/lang/<int:lid>/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/'.format(uid, lid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_add_user_lang(self):
        ''' Test of status code of lang
        '/user/<int:uid>/lang/add/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/add/'.format(uid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_edit_user_lang(self):
        ''' Test of status code of edit a lang
        '/user/<int:uid>/lang/<int:lid>/edit/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/edit/'.format(uid, lid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_del_user_lang(self):
        ''' Test of status code of deleting a lang
        '/user/<int:uid>/lang/<int:lid>/del/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/del/'.format(uid, lid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_add_user_text(self):
        ''' Test of status code of adding a text
        '/user/<int:uid>/lang/<int:lid>/text/add/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/text/add/'
                .format(uid, lid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_edit_user_text(self):
        ''' Test of status code of editing a text
        '/user/<int:uid>/lang/<int:lid>
        /text/<int:tid>/edit/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        tid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/text/{2}/edit/'
                .format(uid, lid, tid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_del_user_text(self):
        ''' Test of status code of deleting a text
        '/user/<int:uid>/lang/<int:lid>
        /text/<int:tid>/edit/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        tid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/text/{2}/del/'
                .format(uid, lid, tid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_text_index(self):
        ''' Test of status code of showing a text with both audio and writing
        '/user/<int:uid>/lang/<int:lid>/text/<int:tid>/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        tid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/text/{2}/'
                .format(uid, lid, tid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_text_both(self):
        ''' Test of status code of showing a text with both audio and writing
        '/user/<int:uid>/lang/<int:lid>/text/<int:tid>/both/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        tid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/text/{2}/both/'
                .format(uid, lid, tid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_text_writing(self):
        ''' Test of status code of showing a text writing
        '/user/<int:uid>/lang/<int:lid>/text/<int:tid>/writing/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        tid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/text/{2}/writing/'
                .format(uid, lid, tid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_text_audio(self):
        ''' Test of status code of showing a text audio
        '/user/<int:uid>/lang/<int:lid>/text/<int:tid>/audio/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        lid = randint(1, 100)
        tid = randint(1, 100)
        response = test_client.\
            get('/user/{0}/lang/{1}/text/{2}/audio/'
                .format(uid, lid, tid),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_login(self):
        ''' Test of status code of '/login/' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/login/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_logout_id(self):
        ''' Test of status code of user logout '/logout/<int:uid>/'
        '''
        test_client = app.test_client(self)
        uid = randint(1, 100)
        response = test_client.get('/logout/{0}/'.format(uid),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
