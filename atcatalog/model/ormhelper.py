# -*- coding: utf-8 -*-
'''
orm helper functions and classes
'''

from sys import stdout

# Decorator for unicode representation taken from:
# http://stackoverflow.com/questions/3627793/
def force_encoded_string_output(func):
    '''
    Best output type and encoding practices for repr functions
    to have encoded __repr__
    Only needed for python 2
    '''
    def _func(*args, **kwargs):
        return func(*args, **kwargs).encode(stdout.encoding or 'utf-8')
    return _func

# Idea and code base for unique objects in database taken from
# https://bitbucket.org/zzzeek/sqlalchemy/wiki/UsageRecipes/UniqueObject
# Simplified and contracted
class UniqueMixin(object):
    '''
    Class for creating unique session objects
    A new object is only created if it isn't
    already in the database
    '''
    @staticmethod
    def _unique(session, cls, arg, kw):
        '''
        Gets the session cache and checks if object
        is already in there. Returns finding
        or new if not found
        '''
        
        # check if there is a session cache
        # otherwise create an empty one
        cache = getattr(session, '_unique_cache', None)
        if cache is None:
            session._unique_cache = cache = {}

        # create a key based on the hash function
        key = (cls, cls.unique_hash(*arg, **kw))
        
        # if found just return our object
        if key in cache:
            return cache[key]
        # the object might not be in the cache
        # so query the database
        else:
            with session.no_autoflush:
                query = session.query(cls)
                query = cls.unique_filter(query, *arg, **kw)
                obj = query.first()
                # obj still not there then create it
                # and add it to the session
                if not obj:
                    obj = cls(*arg, **kw)
                    session.add(obj)
            cache[key] = obj
            return obj

    @classmethod
    def unique_hash(cls, *arg, **kw):
        raise NotImplementedError()

    @classmethod
    def unique_filter(cls, query, *arg, **kw):
        raise NotImplementedError()

    @classmethod
    def as_unique(cls, session, *arg, **kw):
        return UniqueMixin._unique(
                    session,
                    cls,
                    arg, 
                    kw
               )
