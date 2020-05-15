def max(data):
    highest = 0
    for d in data:
        if d > highest:
            highest = d
    return highest


data = [1, 2, 3]
assert max(data) == 3, 'fail'
