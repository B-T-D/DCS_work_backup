
def get_new_index(sorted_list, item, left, right):
    """Uses binary search to return the index position of the item that would
    immediately follow item if it were already in the list. The value to pass
    to builtin list.insert(index, item). 

    Returns:
        (int): index of the item immediately following where item would go
    """
    
    if item > sorted_list[-1]: # base case where item would go at end
        return len(sorted_list)
    elif left > right:
        return left # base case where item would go somewhere else in the list
    mid = (left + right) // 2
    if item == sorted_list[mid]:
        raise ValueError # item is not supposed to already be in the list
    if item < sorted_list[mid]:
        return get_new_index(sorted_list, item, left, mid - 1) # 1st half
    return get_new_index(sorted_list, item, mid + 1, right)

def insert(sorted_list, item):
    """Inserts an item into a sorted list, maintaining the sorted order,
    without re-sorting the list.

    Args:
        sorted_list (list): a list object that has been sorted
        item: the item to insert in the list

    Returns:
        None
    """
    new_index = get_new_index(sorted_list, item, 0, len(sorted_list))
    sorted_list.insert(new_index, item)

def solman(data, item):
    index = 0
    while (index < len(data)) and (data[index] < item):
        index = index + 1
    data.insert(index, item)

sorted_list = [1, 2, 4, 5]
item = 3
expected = 2
actual = get_new_index(sorted_list, item, 0, len(sorted_list))
assert actual == expected, f"actual {actual}, expected {expected}"

sorted_list = [1, 2, 4, 5]
item = 6
expected = 4
actual = get_new_index(sorted_list, item, 0, len(sorted_list))
assert actual == expected, f"actual {actual}, expected {expected}"

print("Passed binary search function tests")

print('--------')
item = 3
expected = [1, 2, 3, 4, 5]
insert(sorted_list, item)
actual = sorted_list
assert actual == expected, f"actual {actual}, expected {expected}"

sorted_list = [1, 2, 4, 5]
item = 6
expected = [1, 2, 4, 5, 6]
insert(sorted_list, item)
actual = sorted_list
assert actual == expected, f"actual {actual}, expected {expected}"

sorted_list = [1, 2, 4, 5]
item = -2
expected = [-2, 1, 2, 4, 5]
insert(sorted_list, item)
actual = sorted_list
assert actual == expected, f"actual {actual}, expected {expected}"


print("Passed insert function tests")
print('---------')

sorted_list = [1, 2, 4, 5]
sm_list = sorted_list.copy()
item = 3
solman(sm_list, item)
expected = sm_list
insert(sorted_list, item)
actual = sorted_list
assert actual == expected, f"actual {actual}, expected {expected}"

sorted_list = [1, 2, 4, 5]
sm_list = sorted_list.copy()
item = 6
solman(sm_list, item)
expected = sm_list
insert(sorted_list, item)
actual = sorted_list
assert actual == expected, f"actual {actual}, expected {expected}"


print("Passed tests against solutions manual")

