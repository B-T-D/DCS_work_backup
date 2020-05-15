#!/usr/bin/env python3

import urllib.request as web

def readQuakes():
    pass
    
def swap(data, i, j):
    pass

def selectionSort(keys, data):
    """Sort parallel lists of keys and data values in ascending 
       order using the selection sort algorithm.
    
    Parameters:
        keys: a list of keys
        data: a list of data values corresponding to the keys
        
    Return value: None
    """
    
    n = len(keys)
    for start in range(n - 1):
        minIndex = start
        for index in range(start + 1, n):
            if keys[index] < keys[minIndex]:
                minIndex = index
        swap(keys, start, minIndex)
        swap(data, start, minIndex)
        
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
    if target == keys[mid]:       # base case 2: found
        return mid
    if target < keys[mid]:        # recursive cases
        return binarySearch(keys, target, left, mid - 1)  # 1st half
    return binarySearch(keys, target, mid + 1, right)     # 2nd half

def queryQuakes(ids, data):
    key = input('Earthquake ID (q to quit): ')
    while key != 'q':
        index = binarySearch(ids, key, 0, len(ids) - 1)
        if index >= 0:
            print('Location: ' + str(data[index][:2]) + '\n' +
                  'Magnitude: ' + str(data[index][3]) + '\n' +
                  'Depth: ' + str(data[index][2]) + '\n')
        else:
            print('An earthquake with that ID was not found.')
        key = input('Earthquake ID (q to quit): ')

def main():
    ids, data = readQuakes()    # left as an exercise
    selectionSort(ids, data)
    queryQuakes(ids, data)
    
main()
