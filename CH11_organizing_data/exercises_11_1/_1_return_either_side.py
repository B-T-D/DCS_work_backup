"""Modify the two binary search algorithms (iterative and recursive versions)
to return the values on either side of target when target is not found."""

def binary_search(keys, target, left, right):
    """Recursive version of binary search function.

    Args:
        left (int): the starting index in the list slice to search
        right (int): the ending index of the list slice to search
            i.e. a slice of keys

    Retrns:
        (int): index value of occurrence of target in keys, else the
            values of the items on either side if target not in keys.
    """

    if left > right: # base case 1: not found
        try:
            return keys[right], keys[left]
        except IndexError:
            return keys[right], keys[0] # Does this make sense for what to return if item would be at end?
    mid = (left + right) // 2
    if target == keys[mid]: # base case 2: found
        return mid
    if target < keys[mid]:
        return binary_search(keys, target, left, mid - 1) # 1st half
    return binary_search(keys, target, mid + 1, right) # 2nd half

def binary_search_1(keys, target):
    """Find the index of target in a sorted list of keys.

    Args:
        keys (list): a list of key values
        target: a value for which to search

    Returns:
        (int): the index of an occurrence of target in keys.
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
    return keys[right], keys[left]
        

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


print(f"----Tests for recursive version----")
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
target = 'c'
expected = 2
actual = binary_search(keys, target, 0, len(keys) - 1)
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"ok on simple case of finding something that's in the keys")

target = 'da'
expected = ('d', 'e')
actual = binary_search(keys, target, 0, len(keys) - 1)
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"ok on simple test case of value not in keys")

keys = ['a', 'b', 'c', 'e', 'f', 'g']
target = 'd'
expected = ('c', 'e')
actual = binary_search(keys, target, 0, len(keys) - 1)
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"ok on second simple case ('d' removed from the original keys)")

keys = ['a', 'b', 'c', 'e', 'f', 'g']
target = 'h'
expected = ('g', 'a')
actual = binary_search(keys, target, 0, len(keys) - 1)
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"ok for case target would be last item in the sorted list")

print(f"----Tests for iterative version----")
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
target = 'c'
expected = 2
actual = binary_search_1(keys, target)
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"ok on simple case of finding something that's in the keys")

target = 'da'
expected = ('d', 'e')
actual = binary_search_1(keys, target)
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"ok on simple test case of value not in keys")
