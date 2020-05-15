def search(data, target):
    """Returns the index of target if it's found in the list data, else -1"""
    for d in range(0, len(data)):
        if data[d] == target:
            return d
    return -1 



data = ['Tris', 'Tobias', 'Caleb']
assert search(data, 'Tris') == 0, 'fail, Tris is at [0]'
assert search(data, 'Peter') == -1, "fail, peter isn't in"
