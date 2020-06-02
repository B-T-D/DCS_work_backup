
def insertion_sort_parallel(keys, data):
    """

    Returns:
        None
    """
    assert len(keys) == len(data), "Number of keys must equal number of data \
elements"
    n = len(keys)
    for insert_index in range(1, n):
        key_to_insert = keys[insert_index]
        data_to_insert = data[insert_index]
        index = insert_index - 1
        while index >= 0 and keys[index] > key_to_insert:
            keys[index + 1] = keys[index]
            data[index + 1] = data[index]
            index = index - 1
        keys[index + 1] = key_to_insert
        data[index + 1] = data_to_insert
        
    

keys = [3, 4, 1, 0, 2]
data = ['d', 'e', 'b', 'a', 'c']
expected_keys = [0, 1, 2, 3, 4]
expected_data = ['a', 'b', 'c', 'd', 'e']

insertion_sort_parallel(keys, data)
actual_keys = keys
actual_data = data

assert actual_keys == expected_keys, f"actual {actual_keys}, expected {expected_keys}"
assert actual_data == expected_data, f"actual {actual_data}, expected {expected_data}"
