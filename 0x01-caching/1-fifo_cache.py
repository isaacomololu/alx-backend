#!/usr/bin/python3
""" FIFO caching system """

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    ''' Represents FIFO caching system to store and retrieve data.
    '''
    def __init__(self):
        ''' Initialize
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                key, _ = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(key))

    def get(self, key):
        ''' Get an item by key
        '''
        return self.cache_data.get(key, None)
