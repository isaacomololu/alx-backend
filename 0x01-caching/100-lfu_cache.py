#!/usr/bin/python3
""" LFU caching system """

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    ''' Represents LFU caching system to store and retrieve data.
    '''
    def __init__(self):
        ''' Initialize
        '''
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_counts = {}

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is not None and item is not None:
            if key not in self.cache_data:
                if (len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS):
                    # Find the item with the lowest usage count
                    lfu_key = min(self.usage_counts, key=self.usage_counts.get)
                    self.cache_data.pop(lfu_key)
                    self.usage_counts.pop(lfu_key)
                    print('DISCARD: {}'.format(lfu_key))
            self.cache_data[key] = item
            self.usage_counts[key] = self.usage_counts.get(key, 0) + 1

    def get(self, key):
        ''' Get an item by key
        '''
        if key in self.cache_data:
            self.usage_counts[key] = self.usage_counts.get(key, 0) + 1
        return self.cache_data.get(key, None)
