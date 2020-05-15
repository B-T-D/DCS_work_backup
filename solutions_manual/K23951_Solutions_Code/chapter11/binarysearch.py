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
        print('left =', left, 'right =', right, 'mid =', mid)
        if target < keys[mid]:
            right = mid - 1
        elif target > keys[mid]:
            left = mid + 1
        else:
            return mid
    return -1

def main():
    keys = [10, 20, 30, 40, 50, 60, 70, 90, 110, 110, 120]
    result = binarySearch(keys, 70)
    print(result)
    result = binarySearch(keys, 72)
    print(result)
    
main()
