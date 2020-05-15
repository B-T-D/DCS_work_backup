#!/usr/bin/env python3

def binarySearch(keys, target, left, right):
    """Recursively find the index of target in a sorted list of keys.
    
    Parameters:
        keys: a list of key values
        target: a value for which to search
        
    Return value: 
        the index of an occurrence of target in keys
    """
    
    if left > right:              # base case 1: not found
        return -1
    mid = (left + right) // 2
    print('left =', left, 'right =', right, 'mid =', mid)
    if target == keys[mid]:       # base case 2: found
        return mid
    if target < keys[mid]:        # recursive cases
        return binarySearch(keys, target, left, mid - 1)  # 1st half
    return binarySearch(keys, target, mid + 1, right)     # 2nd half

def main():
    keys = [10, 20, 30, 40, 50, 60, 70, 90, 110, 110, 120]
    result = binarySearch(keys, 70, 0, len(keys) - 1)
    print(result)
    result = binarySearch(keys, 72, 0, len(keys) - 1)
    print(result)
    
main()