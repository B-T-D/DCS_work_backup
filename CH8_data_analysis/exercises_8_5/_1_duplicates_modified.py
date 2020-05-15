"""Modifiy the remove_duplicates functions so that they instead return a
list of only those items in data that have duplicates."""

def return_duplicates(data):
    """Return a list of the items in data that have appear more than once in
    (list) data."""
    seen = {}
    duplicates = []
    for item in data:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen[item] = True
    return duplicates

data = [1, 2, 3, 1, 3, 1]

duplicates = return_duplicates(data)

assert duplicates == [1, 3], f"Fail, returned {duplicates}"
print("pass")
