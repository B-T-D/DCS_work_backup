#!/usr/bin/env python3

def sumList(data):
    """Compute the sum of the values in a list.
    
    Parameter:
        data: a list of numbers
        
    Return value: the sum of the values in the list
    """

    if len(data) == 0:                  # base case
        return 0
    return data[0] + sumList(data[1:])  # recursive case

#   return sumList(data[:-1]) + data[-1]  # alternative recursive case
