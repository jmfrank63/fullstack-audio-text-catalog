'''
Testfile for testing flask functionallity
'''
from atcatalog import app
import unittest


class Test_flask_routes(unittest.TestCase):
    '''
    Testing flask routes
    '''
    def test_status_index(self):
        '''
        Test of status code of main '/' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_languages(self):
        '''
        Test of status code of languages '/languages' route
        '''
        test_client = app.test_client(self)
        response = test_client.get('/languages/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_status_language(self):
        '''
        Test of status code of language '/language/<int: id>'
        '''
        test_client = app.test_client(self)
        response = test_client.get('/language/1/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
