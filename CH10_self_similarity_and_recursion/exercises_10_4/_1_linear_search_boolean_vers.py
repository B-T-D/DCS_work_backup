def linear_search_b(data, target):
    """Version of the recursive linear search function that returns True
    if the target is contained anywhere in the list, else False."""
    if len(data) == 0:
        return False
    if target == data[0]:
        return True
    return linear_search_b(data[1:], target)


data = [1, 2, 3, 4, 567, 8, 9, 10, 11]
target = 567
expected = True
actual = linear_search_b(data, target)
assert actual == expected, f"actual {actual}, expected {expected}"

target = "Glopp"
expected = False
actual = linear_search_b(data, target)
assert actual == expected, f"actual {actual}, expected {expected}"

