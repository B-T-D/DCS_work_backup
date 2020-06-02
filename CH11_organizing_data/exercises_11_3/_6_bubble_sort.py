
def swap(data, i, j):
    """Swaps the positions of the items with indices i and j in list data.

    Args:
        data (list): a list of values
        i (int): an index of an item in data (not a value)
        j (int): a second index in data
    Returns:
        None
    """
    orig_i = data[i]
    data[i] = data[j]
    data[j] = orig_i

def bubble_sort(data):
    """Implements bubble sort algorithm.


    Returns:
        None
    """
    iterations_count = 0
    for i in range(len(data)):
        for value in data:
            if data.index(value) < len(data) - 1 and value > data[data.index(value) + 1]:
                swap(data, data.index(value), data.index(value) + 1)
##                print(f"data is now {data}")
        iterations_count += 1
    print(f"first version bubble sort outer loop iterated {iterations_count} times")

def solman_bubble_sort(data):
    for last_index in range(len(data) - 1, 0, -1): # Handles the index out of range issue
        for index in range(last_index):
            if data[index] > data[index + 1]:
                swap(data, index, index + 1)
##                print(f"data is now {data}")
                # ^^ confirmed steps happen in same order as mine

def improved_bubble_sort(data):
    """Improved bubble sort implementation that detects when sorting is complete
    and returns early."""
    iterations_count = 0
    swaps_this_time = True
    while swaps_this_time:
        swaps_this_time = False # So it will stay false through end of loop unless retoggled to true
        for value in data:
            if data.index(value) < len(data) - 1 and value > data[data.index(value) + 1]:
                swaps_this_time = True
                swap(data, data.index(value), data.index(value) + 1)
                
                print(f"data is now {data}")
        iterations_count += 1
    print(f"improved bubble sort outer loop iterated {iterations_count} times")
        
def main():
    data = [3, 4, 1, 5, 2]
    expected = [1, 2, 3, 4, 5]
    bubble_sort(data)
    actual = data
    assert actual == expected, f"actual {actual}, expected {expected}"

    print('--------')
    data = [3, 4, 1, 5, 2]
    expected = [1, 2, 3, 4, 5]
    solman_bubble_sort(data)
    actual = data
    assert actual == expected, f"actual {actual}, expected {expected}"

    print(f'-----Improved bubble sort-----')
    data = [3, 4, 1, 5, 2]
    expected = [1, 2, 3, 4, 5]
    improved_bubble_sort(data)
    actual = data
    assert actual == expected, f"actual {actual}, expected {expected}"

    # does the improved one return in fewer steps if the list is just one swap from sorted?
    data = [2, 1, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    improved_bubble_sort(data)
    actual = data
    assert actual == expected, f"actual {actual}, expected {expected}"

    data = [2, 1, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    bubble_sort(data)
    actual = data
    assert actual == expected, f"actual {actual}, expected {expected}"

    # yes, confirmed it iterates fewer times through the outer loop.

    print(f"data already fully sorted:")
    data = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    bubble_sort(data)
    actual = data
    assert actual == expected, f"actual {actual}, expected {expected}"
    # iterates 5 times even when data already fully sorted, so best case O(n)

    data = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    improved_bubble_sort(data)
    actual = data
    assert actual == expected, f"actual {actual}, expected {expected}"
    # versus improved version constant-time best case of 1 iteration through the list
        # That's still not constant time for the full algorithm, just a constant
        # number of iterations. One iteration through the list makes n - 1 compares.

    

if __name__ == '__main__':
    main()
