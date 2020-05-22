def min_list(data):
    """Returns the minimum of the items in the list of numbers data. Ok to use
    built in min function but only for finding the min of *two* numbers."""
    if len(data) <= 2:
        return min(data[0], data[1])
    return min(data[0], min_list(data[1:]))

def solman(data):
    # he does two base cases
    if data == []:
        return None
    if len(data) == 1:
        return data[0]
    return min(data[0], solman(data[1:])) # heart of the recursive case is same as mine

data = [2, 3, 4, 5, 1, 14, 9]
print(data[1:])
control = 1
returned = min_list(data)

assert returned == control, f"returned {returned}"
print(min_list([5, 6, 7, 8, 3]))
print(solman([5, 6, 7, 8, 3]))
