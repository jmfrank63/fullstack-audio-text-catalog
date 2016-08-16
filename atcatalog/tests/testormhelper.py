# -*- coding: utf-8 -*-
'''
Orm helper test cases
Pure to make later use in other sqlalchemy use cases
'''
from atcatalog.model.ormhelper import *
from unittest import main, TestCase
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# We need some sql objects for testing
Base = declarative_base()

class SQLTable(Base, UniqueMixin):
    '''
    A test sql table to test our unique mixin class
    '''
    __tablename__ = 'sql_table'

    id = Column(Integer, primary_key = True)
    field_one = Column(String)
    field_two = Column(String)

    @force_encoded_string_output
    def __repr__(self):
        return "<SQLTable(id= {1}, field_one= {2}, \
        field_two= {3})>".format(self.id,
                                 self.field_one,
                                 self.field_two)


class TestHelperFunctions(TestCase):
    '''
    Test the helper functions
    '''
    def test_force_encoded_string_output(self):
        '''
        Test the string unicode conversion
        This is a very shallow test mainly to keep
        code coverage happy not to test the library function
        "encode" that is called again
        '''
        def test_repr():
            return 'string'

        unicode_repr = force_encoded_string_output(test_repr)
        self.assertEqual(unicode_repr(), u'string')



class TestUniqueMixin(TestCase):
    '''
    Test the UniqueMixin class
    '''
    def setUp(self):
        '''
        Setup a connection pool, scoped session and a declarative base
        '''
        self.test_engine = create_engine('sqlite://')
        self.Session = scoped_session(sessionmaker(bind=self.test_engine))
        self.session = self.Session()
        self.sqlobject = SQLTable(field_one='one', field_two='two')
        self.sqlobject_dif = SQLTable(field_one='1', field_two='2')
        self.sqlobject_dup = SQLTable(field_one='one', field_two='two')
        self.sqlobject_half_one = SQLTable(field_one='one')
        self.sqlobject_half_two = SQLTable(field_two='two')

    def tearDown(self):
        '''
		Teardown the all session and the connection pool
		'''
        self.test_engine.dispose()

    def test_add_object(self):
        '''
        Add an object to the UniqueMixin class
        '''
        

if __name__ == '__main__':
	main()

