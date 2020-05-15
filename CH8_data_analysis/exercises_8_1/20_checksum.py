def checksum(data):
    """Computes a single checksum digit for the list of integers data
    and returns the list with the checksum digit added to the end."""
    new_list = data
    new_list.append(sum(data) % 10)
    return new_list

def check(data):
    correct_sum = sum(data[:-1]) % 10
    return True if data[-1] == correct_sum else False

data = [4, 8, 6, 7, 3]
data2 = checksum(data)
print(data2)
print(check(data2))
assert check(data) == True, 'fail'
