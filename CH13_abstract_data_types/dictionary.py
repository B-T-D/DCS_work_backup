
class Dictionary:
    """A dictionary class."""

    _KEY = 0 # index of key in each pair (all pairs are two elements)
    _VALUE = 1 # index of value in each pair
    # ^ book defines these here as class variables rather than as instance
    #   variables in init. This makes them shared by every object in the class.
    #   Rather than needing separate, repetititve instance of _KEY and _VALUE
    #   for every instance of a dictionary object. _KEY and _VALUE are always
    #   0 and 1 no matter what else is in the dictionary. 
    
    def __init__(self):
        """Construct a new Dictionary object."""
        self._length = 0 # number of (key, value) pairs
        self._size = 11 # number of slots in the hash table
        self._table = [None] * self._size # hash table containing (key, value) pairs
##        self._KEY = 0 # index of key in each pair (all pairs are two elements)
##        self._VALUE = 1 # index of value in each pair

    def _hash(self, key):
        return key % self._size

    def __setitem__(self, key, value):
        """Insert a key:value pair into self."""

        index = self._hash(key)
        self._table[index] = (key, value)
        self._length = self._length + 1

    def __delitem__(self, key):
        """Delete the pair with the given key."""
        index = self._hash(key)
        if self._table[index] != None and self._table[index][self._KEY] == key:            
            # ^ Second condition is because even if the value isn't None,
            #   some other key paired with a different value could live there.
            self._table[index] = None
            self._length -= 1
        else:
            raise KeyError('Key was not found')

    def __getitem__(self, key):
        """Return the value associated with key."""
        index = self._hash(key)
        if self._table[index] != None and self._table[index][self._KEY] == key:
            return self._table[index][self._VALUE]
        else:
            raise KeyError('Key was not found')

    def __len__(self):
        """Return the number of (key, value) pairs."""
        return self._length

    def is_empty(self):
        """Return True if the dictionary is empty else False."""
        return len(self) == 0
        

def main():
    wseries = Dictionary()
    wseries[1903] = 'Boston Americans'
    wseries[1979] = 'Pittsburgh Pirates'
    wseries[2014] = 'San Francisco Giants'
    print(wseries[1979])
    del wseries[2014]
    print(len(wseries))
    try:
        print(wseries[2014])
    except:
        print(f"__getitem__ on key=2014 raised key error as expected")

if __name__ == '__main__':
    main()
