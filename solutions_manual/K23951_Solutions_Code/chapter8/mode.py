#!/usr/bin/env python3

def mode(data):
    """Compute the mode of a non-empty list.
    
    Parameter:
        data: a list of items
        
    Return value: the mode of the items in data
    """
    
    frequency = { }
    
    for item in data:
        if item in frequency:
            frequency[item] = frequency[item] + 1
        else:
            frequency[item] = 1

    frequencyValues = list(frequency.values())
    maxFrequency = max(frequencyValues)
    
    modes = [ ]
    for key in frequency:
        if frequency[key] == maxFrequency:
            modes.append(key)
    
    return modes
