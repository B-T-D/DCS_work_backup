def linear_search(data, target, first):
    """New version of the recursive linear search algorithm that only looks
    at every other item in the list for the target value."""
    if (first < 0) or (first >= len(data)):
        return -1
    if target == data[first]:
        return first
    return linear_search(data, target, first + 2)
    
    pass

data = [1, 2, 3, 4, 2] # Book's example 
expected = 4 # Wouldn't find the 2 at data[1]
actual = linear_search(data, 2, 0)
assert actual == expected, f"actual {actual}, expected {expected}"
