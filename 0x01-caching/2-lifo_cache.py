#!/usr/bin/python3
""" LIFO caching system """

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    ''' Represents LIFO caching system to store and retrieve data.
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
            if key not in self.cache_data:
                if (len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS):
                    rear_key, _ = self.cache_data.popitem(True)
                    print('DISCARD: {}'.format(rear_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        ''' Get an item by key
        '''
        return self.cache_data.get(key, None)
