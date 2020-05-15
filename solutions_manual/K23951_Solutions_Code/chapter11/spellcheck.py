#!/usr/bin/env python3

def binarySearch(keys, target):
    """Find the index of target in a sorted list of keys.
    
    Parameters:
        keys: a list of key values
        target: a value for which to search
        
    Return value: 
        the index of an occurrence of target in keys
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

def spellcheck():
    """Repeatedly ask for a word to spell-check and print the result.
    
    Parameters: none
    
    Return value: None
    """
    
    dictFile = open('/usr/share/dict/words', 'r', encoding = 'utf-8')
    dictionary = [ ]
    for word in dictFile:
        dictionary.append(word[:-1])
    dictFile.close()
    dictionary.sort()
    
    word = input('Enter a word to spell-check (q to quit): ')
    while word != 'q':
        index = binarySearch(dictionary, word)
        if index != -1:
            print(word, 'is spelled correctly.')
        else:
            print(word, 'is not spelled correctly.')
        print()
        word = input('Enter a word to spell-check (q to quit): ')
        
def main():
    spellcheck()
    
main()
