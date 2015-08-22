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
        '''
        Test of status code of main '/' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_languages(self):
        '''
        Test of status code of languages '/languages' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/languages/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_language(self):
        '''
        Test of status code of language '/language/<int:language_id>'
        '''
        test_client = app.test_client(self)
        language_id = randint(1, 100)
        response = test_client.get('/language/{0}/'.format(language_id),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_language_texts(self):
        '''
        Test of status code of language '/language/<int:language_id>/texts'
        '''
        test_client = app.test_client(self)
        language_id = randint(1, 100)
        response = test_client.get('/language/{0}/texts/'.format(language_id),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_index(self):
        '''
        Test of status code of language
        '/user/<int:user_id>/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        response = test_client.get('/user/{0}/'.format(user_id),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_languages(self):
        '''
        Test of status code of language
        '/user/<int:user_id>/languages/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        response = test_client.get('/user/{0}/languages/'.format(user_id),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_language_texts(self):
        '''
        Test of status code of language
        '/user/<int:user_id>/language/<int:language_id>/texts/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        language_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/{1}/texts/'.format(user_id, language_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_show_user_language_index(self):
        '''
        Test of status code of language
        '/user/<int:user_id>/language/<int:language_id>/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        language_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/{1}/'.format(user_id, language_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_add_user_language(self):
        '''
        Test of status code of language
        '/user/<int:user_id>/language/add/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/add/'.format(user_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_edit_user_language(self):
        '''
        Test of status code of edit a language
        '/user/<int:user_id>/language/<int:language_id>/edit/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        language_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/{1}/edit/'.format(user_id, language_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_delete_user_language(self):
        '''
        Test of status code of deleting a language
        '/user/<int:user_id>/language/<int:language_id>/delete/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        language_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/{1}/delete/'.format(user_id, language_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_add_user_text(self):
        '''
        Test of status code of adding a text
        '/user/<int:user_id>/language/<int:language_id>/text/add/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        language_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/{1}/text/add/'
                .format(user_id, language_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_edit_user_text(self):
        '''
        Test of status code of editing a text
        '/user/<int:user_id>/language/<int:language_id>
        /text/<int:text_id>/edit/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        language_id = randint(1, 100)
        text_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/{1}/text/{2}/edit/'
                .format(user_id, language_id, text_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_delete_user_text(self):
        '''
        Test of status code of deleting a text
        '/user/<int:user_id>/language/<int:language_id>
        /text/<int:text_id>/edit/'
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        language_id = randint(1, 100)
        text_id = randint(1, 100)
        response = test_client.\
            get('/user/{0}/language/{1}/text/{2}/delete/'
                .format(user_id, language_id, text_id),
                content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_login(self):
        '''
        Test of status code of '/login/' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/login/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_logout_id(self):
        '''
        Test of status code of '/logout/<int: user_id>/' routes
        '''
        test_client = app.test_client(self)
        user_id = randint(1, 100)
        response = test_client.get('/logout/{0}/'.format(user_id),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
