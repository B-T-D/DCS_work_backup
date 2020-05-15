#!/usr/bin/env python3

class Dictionary:
    """A dictionary class."""
    
    _KEY = 0     # index of key in each pair
    _VALUE = 1   # index of value in each pair

    def __init__(self):
        """Construct a new Dictionary object."""

        self._length = 0     # number of key:value pairs
        self._size = 11      # number of slots in the hash table
        self._table = [None] * self._size  # hash table containing
                                           #  (key, value) pairs
    def _hash(self, key):
        return key % self._size
            
    def __len__(self):
        """Return the number of (key, value) pairs."""
        
        return self._length
                
    def isEmpty(self):
        """Return true if the dictionary is empty, false otherwise."""

        return len(self) == 0
        
    def __setitem__(self, key, value):
        """Insert a (key, value) pair into self."""

        index = self._hash(key)
        self._table[index] = (key, value)
        self._length = self._length + 1

    def __delitem__(self, key):
        """Delete the pair with a given key."""

        index = self._hash(key)
        if self._table[index] != None and \
           self._table[index][self._KEY] == key:
            self._table[index] = None
            self._length = self._length - 1
        else:
            raise KeyError('key was not found')

    def __getitem__(self, key):
        """Return the value associated with a key."""

        index = self._hash(key)
        if self._table[index] != None and \
           self._table[index][self._KEY] == key:
            return self._table[index][self._VALUE]
        else:
            raise KeyError('key was not found')
 
def main():    
    worldSeries = Dictionary()
    worldSeries[1903] = 'Boston Americans'
    worldSeries[1979] = 'Pittsburgh Pirates'
    worldSeries[2014] = 'San Francisco Giants'
    print(worldSeries[1979])  # prints "Pittsburgh Pirates"
    del worldSeries[2014]
    print(len(worldSeries))   # prints 2
#   print(worldSeries[2014])  # KeyError
    
main()
help(Dictionary)