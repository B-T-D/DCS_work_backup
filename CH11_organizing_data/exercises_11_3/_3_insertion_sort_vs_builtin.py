import time

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

def compare():
    """Compares the time required to sort a long list of english words using
    insertion sort to the time required by the sort method of the list class."""
    filename = r"C:\Users\Ben\Desktop\Python_DCS_book\CH11_organizing_data\words.txt"
    file = open(filename, mode='r', encoding='utf-8')
    words = [line.rstrip() for line in file.readlines()]
##    words = ['z', 'a', 'b', 'c', 'h', 'm', 'f', 'i']
    words_1 = words.copy()
    start = time.time()
    insertion_sort(words_1)
    end = time.time()
    elapsed_insertion = end - start

    words_2 = words.copy()
    assert words_2 == words
    start = time.time()
    words_2.sort()
    end = time.time()
    elapsed_builtin = end - start

    print(f"words_2 == words_1 --> {words_2 == words_1}")

    print(f"Insertion sort: {elapsed_insertion}\n \
Builtin list.sort() merge sort algorithm: {elapsed_builtin}")

compare()
