

def square(data):
    """Takes a list of numbers data and squares each number in place without
    returning anything."""

    for i in range(len(data)):
        data[i] = data[i] ** 2


data = [2, 3, 4, 5]

square(data)
print(data)
assert data == [4, 9, 16, 25], 'fail'
