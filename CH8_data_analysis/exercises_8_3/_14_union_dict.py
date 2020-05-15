# solman seems more elegant. Just copy dict1, because we know everything in
# dict1 (every kv pair) will be in the new returned dict exactly as-is.

def union(dict1, dict2):
    """Returns a new dictionary that contains all of the entries of the two
    dictionaries dict1 and dict2. If the dictionaries share a key, use the
    first dict's value for that key."""
    union = {}
    for key in dict1:
        union[key] = dict1[key]
    for key in dict2:
        if key not in union:
            union[key] = dict2[key]
    return union

def sol_man(dict1, dict2):
    union = dict1.copy()
    for key in dict2:
        if key not in union:
            union[key] = dict2[key]
    return union

dict1 = {'pies': 3, 'cakes': 5}
dict2 = {'cakes': 4, 'tarts': 2}
correct_return = {'pies': 3, 'cakes': 5, 'tarts': 2}

union = union(dict1, dict2)
assert union == correct_return, f"fail, returned: \n\t{union}"
