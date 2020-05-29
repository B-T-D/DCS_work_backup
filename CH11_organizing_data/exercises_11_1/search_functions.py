def binary_search(keys, target, left, right):
    """Recursive version of binary search function.

    Args:
        left (int): the starting index in the list slice to search
        right (int): the ending index of the list slice to search
            i.e. a slice of keys

    Retrns:
        (int): index value of occurrence of target in keys, else -1
            if target not in keys.
    """

    if left > right: # base case 1: not found
        return -1
    mid = (left + right) // 2
    if target == keys[mid]: # base case 2: found
        return mid
    if target < keys[mid]:
        return binary_search(keys, target, left, mid - 1) # 1st half
    return binary_search(keys, target, mid + 1, right) # 2nd half

def binary_search_iter(keys, target):
    """Find the index of target in a sorted list of keys.

    Args:
        keys (list): a list of key values
        target: a value for which to search

    Returns:
        (int): the index of an occurrence of target in keys
    """

    n = len(keys)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if target < keys[mid]:
             right = mid - 1
        elif target > keys[mid]:
            left = mid + 1
        else:
            return mid
    return -1

def linear_search(keys, target, first=0):
    """"Recursively find the index of the first occurence of target in keys.

    Args:
        keys (list): a list object to search in
        target: value to search for in keys
        first (int): index of first item in keys. Defaults to 0

    Returns:
        (int): index of the first occurrence of target in keys or -1
            if not found.
    """
    if (first < 0) or (first >= len(keys)): # base case 1: not found
        return -1
    if target == keys[first]: # base case 2: found
        return first
    return linear_search(keys, target, first + 1) # recursive case

def spellcheck():
    """Repeatedly ask for a word to spell-check and print the result.

    Args:
        None

    Returns:
        None
    """

    dict_file = open('words.txt', 'r', encoding = 'utf-8')
    word_list = []

    for word in dict_file:
        word_list.append(word[:-1]) # Why slice it? Best guess is avoid newline chars
    dict_file.close()
    word_list.sort()

    word = input('Enter a word to spell-check (q to quit): ')
    while word.lower() != 'q':
        index = binary_search(word_list, word, left=0, right=len(word_list) - 1)
        if index != -1:
            print(word, 'is spelled correctly.')
        else:
            print(word, 'is mispelled.')
        print()
        word = input('Enter a word to spell-check (q to quit): ')


def main():
    spellcheck()

if __name__ == '__main__':
    main()
