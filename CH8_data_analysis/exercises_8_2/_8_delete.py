"""Don't need to accumulate new list in multiple lines with two for loops.
Can combine slices of the original list in a single line and return it. Returning
that means returning a new list object."""

def delete(data, index):
    """Returns a new list that contains the same elements as the list data
    except for the one at the given index. If value of index is negative or
    exceeds len(data), return copy of the original list."""
    if index < 0 or index >= len(data):
        return data.copy()
    new_data = []
    for d in data[:index]:
        new_data.append(d)
    for d in data[index + 1:]:
        new_data.append(d)
    return new_data

def sol_man(data, index):
    if (index < 0) or (index >= len(data)): # >= because e.g. index of 5, len of 5 would mean [5] refers to 6th item in a 5 element list.
        return data.copy()
    return data[:index] + data[index + 1:]
data = [3, 1, 5, 9]

new_data = delete(data, 2)

assert new_data == [3, 1, 9], f"fail {new_data}"
print(f"data is still {data}, function didn't mutate it")

# when index is negative:
assert delete(data, -1) == data, f"fail returned {delete(data, -1)}"


assert sol_man(data, 2) == [3, 1, 9]
assert sol_man(data, -1) == data
assert data == [3, 1, 5, 9], f"Fail, original list data shouldn't have been mutated \
but evaluates to {data}"
