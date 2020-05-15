import random

def linear_search(data, target):
    """Find the index of the first occurrence of target in data.

    Args:
        data (list): A list object to search in
        target (same type as data's elements): An object to search for

    Returns:
        (int): Indes of the first occurence of target in data
    """
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1

def linear_search_all(data, target, start):
    """Differs from above gy (1) returning a list of indices instead of a
    single index and (2) requiring third parameter that specifies where
    the search should begin.

    Args:
        data (list): A list object to search in
        target (same type as data's elements): An object to search for
        start (int): Index at which to begin the search, i.e. to search forward
            from. 
    Returns:
        (list): List of integers representing the indices in data at which
            value equals target
    """
    matches = []
    for index in range(start, len(data)):
        if data[index] == target:
            matches.append(index)
    return matches # book doesn't care about returning -1 if no matches here

def remove_duplicates_1(data):
    """
    Return a list containing only the unique items in data.

    Args:
        data (list): A list

    Returns:
        (list): New list of the unique values in data, in their original order
    """
    
    duplicate_indices = []
    unique = []
    for index in range(len(data)):
        if linear_search(duplicate_indices, index) == -1: # If it's not already a known duplicate
            positions = linear_search_all(data, data[index], index + 1) # index + 1 to check every later in the list item
            duplicate_indices.extend(positions) # using list.extend() because linear_search_all returns a list
            unique.append(data[index]) # if the "if" condition is True, then this is first time we've seen this item
    return unique

def remove_duplicates_2(data):
    """
    """
    # Simplify by not using the duplicate indices list, just search in (list) unique instead.
        # Also don't need to store indices anymore. So can just iterate the values directly.
    unique = []
    for item in data:
        if linear_search(unique, item) == -1:
            unique.append(item)
    return unique

def remove_duplicates_3(data):
    """
    """
    # Uses a dict to track which values have already been seen, so that uniqueness can be checked in
    #   constant time (since a python dict-access operation runs in constant time)
    seen = {}
    unique = []
    for item in data:
        if item not in seen:
            unique.append(item)
            seen[item] = True # This is basically a nonsense filler value (we never check True vs. false, just "in", the point is to use a dict
                # rather than a list because the hash table implementation of dicts makes accesses faster
    return unique

random.seed(3)
data = []
for i in range(100):
    data.append(random.randint(1, 5))
original_data = data.copy()

assert remove_duplicates_1(data) == remove_duplicates_2(data) == remove_duplicates_3(data), f"fail"
assert data == original_data, f"fail data shouldn't have been mutated"
print(f"passed")
    
