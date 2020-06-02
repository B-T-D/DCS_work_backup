

def merge_sort(data):
    """Recursively sort a list in place in ascending order, using the merge
    sort algorithm.

    Args:
        data (list): a list of values to sort

    Returns:
        None
    """

    n = len(data)
    if n > 1: # base case is that single-element list is already sorted
        mid = n // 2
        left = data[:mid]
        right = data[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, data)

def merge(left, right, merged):
    """Merge two sorted lists, named left and right, into one sorted list
    named merged.

    Args:
        left (list): a sorted list
        right (list): a sorted list
        merged (list): the merged sorted list

    Returns:
        None
    """
    merged.clear() # clear the contents of merged
    left_index = 0 # index in left
    right_index = 0 # index in right

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index]) # left value is smaller
            left_index += 1
        else:
            merged.append(right[right_index]) # right value is smaller
            right_index = right_index + 1

    if left_index >= len(left): # items remaining in right
        merged.extend(right[right_index:])
    else:
        merged.extend(left[left_index:]) # items remaining in left
    
def merge_1(left, right, data):
    print(data)
    data = left
    print(data)
    for value in right:
        if value in data:
            data.insert(data.index(value), value)
        elif value > max(data):
            data.append(value)
        elif value < min(data):
            data.insert(0, value)


def main():
    data = [3, 4, 1, 0, 2]
    merge_sort(data)
    print(data)

if __name__ == '__main__':
    main()
    
    
