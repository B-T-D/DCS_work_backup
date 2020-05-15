#!/usr/bin/env python3

def count(text, target):
    """Count the number of target strings in text.
    
    Parameters:
        text: a string object
        target: a string object
        
    Return value: the number of occurrences of target in text 
    """
    
    count = 0
    for index in range(len(text)):
        if text[index:index + len(target)] == target:
            count = count + 1
    return count
