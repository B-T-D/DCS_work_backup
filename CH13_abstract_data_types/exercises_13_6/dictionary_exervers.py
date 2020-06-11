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
        """Exercise 13.6.8, new hash that works for strings.

        Sum the unicode values corresponding to the characters in the string
        and then return the sum mod n."""
        if type(key) == int: # handle int keys same as before
            return key % self._size
        elif type(key) == str:
            int_key = 0
            for character in key:
                int_key += ord(character)
                print(f"ord {character} was {ord(character)}, int_key is now {int_key}")
            print(f"string {key} hashed to {self._hash(int_key)}")
            return self._hash(int_key)
        elif type(key) == tuple:
            # Represent each element in the tuple as an integer, then sum
            # those integers and hash that sum.
            tup_key = 0
            for element in key:
                tup_key += self._hash(element) # To handle elements that are themselves some non-int type
            return self._hash(tup_key)
            

    def old_hash(self, key):
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

    def _print_table(self):
        """Prints the contents of the underlying hash table.

        Including printing hash table slots that only have None.
        """
        for i in range(self._size):
            print(f"{i}: {self._table[i]}")

    def __str__(self):
        """Prints a string representation of the Dictionary object,
        mimicking print() output for a builtin Python dict collection object."""
        string = '{'
        for i in range(0, self._size):
            if self._table[i] != None:
                string += repr(self._table[i][self._KEY]) + ': ' +\
                repr(self._table[i][self._VALUE]) + ', '
        # strip the final superfluous comma+space from end of the string
        #   Probably a more elegant way...
        string = string.rstrip(', ')
        # Book's solution to this (i.e. that you need to treat the last
        #   printed item differently to skip the comma, but blank hash slots
        #   aren't printed at all) is to make a separate list of the items
        #   to print, then add all items except the last to the string,
        #   then add all_items[-1] without a comma (if len(all_items) > 0),
        #   to handle the case of a single element dict or blank dict.
        return string + '}'

    def __contains__(self, key):
        """Return True if a key is contained in the dictionary object, else
        False."""
        index = self._hash(key)
        return self._table[index] != None\
               and self._table[index][self._KEY] # Again: some other key could
                                                # have hashed to that same value
                                                # so can't merely check that it's
                                                # not None and then return

    def items(self):
        """Return the list of key, value tuples."""
        items = []
        for entry in self._table:
            if entry != None:
                items.append(entry)
        return items

    def keys(self):
        """Return a list of keys in self."""
        keys = []
        for entry in self._table:
            if entry != None:
                keys.append(entry[self._KEY])
        return keys

    def values(self):
        """Return a list of the values in self."""
        values = []
        for entry in self._table:
            if entry != None:
                values.append(entry[self._VALUE])
        return values
            
        
        
        

def main():
    import random # not used in the class just here for testing
    wseries = Dictionary()
    wseries[1903] = 'Boston Americans'
    wseries[1979] = 'Pittsburgh Pirates'
    wseries[2014] = 'San Francisco Giants'
    wseries[1740] = 'Provincetown Precogs' # hash 2
    wseries[1621] = 'Plymouth Hat-Bucklers'
    wseries[1851] = 'Edmonton Early-Adopters'
    print(wseries)
    del wseries[2014]
    print(len(wseries))
    try:
        print(wseries[2014])
    except:
        print(f"__getitem__ on key=2014 raised key error as expected")
    wseries._print_table()

    blank = Dictionary()
    print(blank)

    single_element_dict = Dictionary()
    single_element_dict[1] = 'e'
    print(single_element_dict)

    print(1903 in wseries)
    print(1933 in wseries)
    print(f"wseries.items():\n\t{wseries.items()}")
    print(f"wseries.keys():\n\t{wseries.keys()}")
    print(f"wseries.values():\n\t{wseries.values()}")

    print('------')
    print("Exercises 13.6.5 print kv pairs in alphabetical order by key")
    print(sorted(wseries.keys()))
    for key in sorted(wseries.keys()):
        print(str(key) + ": " + wseries[key])

    print('------')
    print("13.6.8 new hash method that works for strings")
    tdict = Dictionary()
    for string in ['foo', 'bar', 'quux', 'kludge']: # quux collides with foo since still only 11 slots
        tdict[string] = random.choice(['baz', 'garply', 'plugh', 17])
    print(tdict)

    print('------')
    print("13.6.9 hash for keys that are tuples")
    tdict = Dictionary()
    random.seed(17)
    tuples = []
    for i in range(10):
        tuples.append((random.randint(0, 99), random.randint(0, 99)))
    for tuple in tuples:
        tdict[tuple] = random.choice(['foo', 'bar', 'baz', 'plugh', 'kludge'])
    print(tdict)
    

if __name__ == '__main__':
    main()
