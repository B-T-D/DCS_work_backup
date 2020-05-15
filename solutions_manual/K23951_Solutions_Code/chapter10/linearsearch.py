#!/usr/bin/env python3

def linearSearch(data, target):
    """Recursively find the index of the first occurrence of 
       target in data.
    
    Parameters:
        data: a list object to search in
        target: an object to search for
        
    Return value: index of the first occurrence of target in data
    """
    
    if (first < 0) or (first >= len(data)):  # base case 1: not found
        return -1
    if target == data[first]:                # base case 2: found
        return first
    return linearSearch(data, target, first + 1) # recursive case
    
