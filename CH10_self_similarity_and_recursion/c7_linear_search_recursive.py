def linear_search(data, target, first=0):
    """Recursively find the index of the first occurrence of target in data.

    Args:
        data (list): a list object to search in
        target: an object to search for (of a type that is among the types of
            data's elements)
        first (int): original index number of the first item in data

    Returns:
        (int) index of the first occurrence of target in data or -1 if not found
    """

    if (first < 0) or (first >= len(keys)): # base case 1: not found
        return -1
    if target == keys[first]: # base case 2: found
        return first # this will have been incremented by the recursive calls
                # such that its value equals the index of the search hit in
                # the full list
    return linear_search(keys, target, first + 1) # recursive case
        # Don't need to arg a slice in the recursive call, because the
        # base case 2 can use the value of first to move through the list


data = [1, 2, 3, 4, 567, 8, 9, 10, 11]
print(linear_search(data, 567))
print(linear_search(data, 'spam'))

    
