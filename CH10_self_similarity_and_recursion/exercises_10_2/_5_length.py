def length(data):
    """Returns length of the list data, recursively, without using len() builtin.
    """
    if data == []:
        return 0
    return 1 + length(data[1:])

data = [1, 2, 3, 4]
control = len(data)
returned = length(data)
assert returned == control, f"returned {returned}"

print(length([3, 2, 1]))
print(length([]))
print(length([1]))
print(length(0))
