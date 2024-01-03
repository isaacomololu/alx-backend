#!/usr/bin/python3
""" Task 0- Basic dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' Represents a caching system to store and retrieve data.
    '''
    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key
        '''
        return self.cache_data.get(key, None)
