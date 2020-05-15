#!/usr/bin/env python3

def binary(length):
    """Return a list of all binary strings with the given length.

    Parameter:
        length: the length of the binary strings

    Return value: 
        a list of all binary strings with the given length
    """

    if length == 0:                          # base case
        return ['']
    
    shorter = binary(length - 1)  # recursively get shorter strings
    
    bitStrings = []                           # create a list
    for shortString in shorter:               #   of bit strings
        bitStrings.append('0' + shortString)  #   with prefix 0

    for shortString in shorter:               # append bit strings
        bitStrings.append('1' + shortString)  #   with prefix 1
        
#   for character in ['0', '1']:                         # more compact version
#       for shortString in shorter:
#           bitStrings.append(character + shortString)
        
    return bitStrings                         # return all bit strings
