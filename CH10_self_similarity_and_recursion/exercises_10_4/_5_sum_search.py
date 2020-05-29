def sum_search(data, total, first):
    """Returns the first index in data, greater than or equal to first, for
    which the sum of the values in data[:index + 1] is greater than or equal
    to total. Returns -1 if sum(data) < total."""
    if sum(data[first:]) < total:
        return -1
    if sum(data[first:first + 1]) >= total:
        return first
    return sum_search(data, total, first + 1)

def solman(data, total, first):
    if (first < 0) or (first >= len(data)):
        return -1
    if data[first] >= total:
        return first
    return solman(data, total - data[first], first + 1)

data = [2, 1, 4, 3]
total = 4
expected = 2
actual = sum_search(data, total, 0)
assert actual == expected, f"actual {actual}, expected {expected}"
actual = solman(data, total, 0)
assert actual == expected, f"actual {actual}, expected {expected}"

total = 14
expected = -1
actual = sum_search(data, total, 0)
assert actual == expected, f"actual {actual}, expected {expected}"
actual = solman(data, total, 0)
assert actual == expected, f"actual {actual}, expected {expected}"

