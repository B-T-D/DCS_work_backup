def insertion_sort(data):
    """Sort a list of values in ascending order using the insertion sort
    algorithm.

    Args:
        (list): a list of values

    Returns:
        None
    """

    n = len(data)
    for insert_index in range(1, n):
        item_to_insert = data[insert_index]
        index = insert_index - 1
        while index >= 0 and data[index] > item_to_insert:
            data[index + 1] = data[index]
            index = index - 1
        data[index + 1] = item_to_insert

def main():
    data = [50, 30, 40, 20, 10, 70, 60]
    print(data)
    insertion_sort(data)
    print(data)

main()
