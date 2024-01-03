#!/usr/bin/python3
""" LRU caching system """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    ''' Represents LRU caching system to store and retrieve data.
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
                    first_key, _ = self.cache_data.popitem(last=False)
                    print('DISCARD: {}'.format(first_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        ''' Get an item by key
        '''
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
