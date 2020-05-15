
def remove(data, value):
    """Returns a new list that contains same elements as data except for those
    that equal value. Should remove all items that equal value not just one."""
    return [d for d in data if d != value]

def sol_man(data, value):
    """Identical to my original brute force / long form solution before
    the list comp"""
    new_data = []
    for item in data:
        if item != value:
            new_data.append(item)
    return new_data

data = [3, 1, 5, 3, 9]
assert remove(data, 3) == [1, 5, 9], f"fail {remove(data, 3)}"
assert data == [3, 1, 5, 3, 9], f"fail, original list was mutated to {data}"

    
