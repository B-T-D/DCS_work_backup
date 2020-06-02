def swap(data, i, j):
    """Swaps the positions of the items with indices i and j in list data.
    Returns:
        None
    """
    orig_i = data[i]
    data[i] = data[j]
    data[j] = orig_i

def selection_sort(data):
    """Sort a list of values in ascending order using the selection sort
    algorithm.

    Args:
        data (list): a list of values

    Returns:
        None
    """

    n = len(data)
    for start in range(n - 1):
        min_index = start
        for index in range(start + 1, n):
            if data[index] < data[min_index]:
                min_index = index
        if min_index != start:
            swap(data, start, min_index)

def selection_sort_parallel_lists(keys, data):
    """Sort parallel lists of keys and data values in ascending order using
    the selection sort algorithm.

    Args:
        keys (list): a list of keys
        data (list): a list of data values corresponding to the keys

    Returns:
        None
    """

    n = len(keys)
    for start in range(n - 1):
        min_index = start
        for index in range(start + 1, n):
            if keys[index] < keys[min_index]:
                min_index = index
        swap(keys, start, min_index)
        swap(data, start, min_index)

def main():
    numbers = [50, 30, 40, 20, 10, 70, 60]
    animals = ['dog', 'cat', 'monkey', 'zebra', 'platypus', 'armadillo']
    heights = [7.80, 6.42, 8.64, 7.83, 7.75, 8.99, 9.25, 8.95]

    print(numbers)
    selection_sort(numbers)
    print(numbers)

    print(animals)
    selection_sort(animals)
    print(animals)

    print(heights)
    selection_sort(heights)
    print(heights)


if __name__ == '__main__':
    main()
    
