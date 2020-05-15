def search(data, target):
    """Returns True if target is in the list data, else False.

    Args:
        data (list): A list of strings
        target (str): String to search for.

    """

    # easy if only searching for exact match...
    for d in data:
        if d == target:
            return True
    return False

data = ['Tris', 'Tobias', 'Caleb']
assert search(data, 'Tris') == True, 'fail, Tris should be in data'
assert search(data, 'Peter') == False, "fail, peter isn't in data"
