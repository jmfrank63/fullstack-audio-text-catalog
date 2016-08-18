# -*- coding: utf-8 -*-
'''
Orm helper test cases
Pure to make later use in other sqlalchemy use cases
'''
from atcatalog.model.ormhelper import *
from unittest import main, TestCase
from sqlalchemy import create_engine, event, Column, Integer, String, and_
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from logging import basicConfig

# For sqlite to force foreign key constraint
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    '''
    Sets the foreign key constraint for sqlite
    '''
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# Create basic logging for sqlite
basicConfig()

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

    @classmethod
    def unique_hash(cls, field_one, field_two):
        return field_one, field_two

    @classmethod
    def unique_filter(cls, query, field_one, field_two):
        return query.filter(and_(SQLTable.field_one == field_one, \
                                 SQLTable.field_two == field_two))

    @force_encoded_string_output
    def __repr__(self):
        return u"<SQLTable(id= {0}, field_one= {1}, \
field_two= {2})>".format(self.id, self.field_one, self.field_two)


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
    Test the pure UniqueMixin class
    '''
    def test_hash_not_implemented(self):
        '''
        Test if unique_hash classmethod is not implemented
        '''
        with self.assertRaises(NotImplementedError):
            UniqueMixin.unique_hash(self)

    def test_filter_not_implemented(self):
        '''
        Test if unique_filter classmethod is not implemented
        '''
        with self.assertRaises(NotImplementedError):
            UniqueMixin.unique_filter(self, None)

class TestUniqueness(TestCase):
    '''
    Test the UniqueMixin class
    '''
    def setUp(self):
        '''
        Setup a connection pool, scoped session and a declarative base
        '''
        self.engine = create_engine('sqlite://')
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        '''
		Teardown the all session and the connection pool
		'''
        self.engine.dispose()

    def test_duplicate_object(self):
        '''
        Add an object twice to the UniqueMixin class
        and test they are the same
        '''
        self.sqlobject = SQLTable.as_unique(self.session,
                                            field_one='one',
                                            field_two='two')
        self.sqlobject_dup = SQLTable.as_unique(self.session,
                                            field_one='one',
                                            field_two='two')
        self.assertIs(self.sqlobject, self.sqlobject_dup)
        self.session.commit()

    def test_non_duplicate_object(self):
        '''
        Add two different objects to the UniqueMixin class
        and test they are different
        '''
        self.sqlobject = SQLTable.as_unique(self.session,
                                            field_one='one',
                                            field_two='two')
        self.sqlobject_dif = SQLTable.as_unique(self.session,
                                            field_one='three',
                                            field_two='two')
        self.assertIsNot(self.sqlobject, self.sqlobject_dif)
        self.session.commit()

    def test_duplicate_after_commit(self):
        '''
        Add a duplicate object to a commited one
        and test if same object
        '''
        self.sqlobject = SQLTable.as_unique(self.session,
                                            field_one='one',
                                            field_two='two')
        self.session.commit()
        self.sqlobject_read = self.session.query(SQLTable).first()
        self.sqlobject_dup = SQLTable.as_unique(self.session,
                                            field_one='one',
                                            field_two='two')
        self.assertIs(self.sqlobject_read, self.sqlobject_dup)
        self.session.commit()

    def test_repr_unicode(self):
        '''
        Test representation is unicode
        '''
        self.sqlobject = SQLTable.as_unique(self.session,
                                            field_one='one',
                                            field_two='two')
        self.assertIsInstance(self.sqlobject.__repr__(), str)
        self.session.commit()

if __name__ == '__main__':
	main()

