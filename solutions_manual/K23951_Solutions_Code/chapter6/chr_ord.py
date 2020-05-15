#!/usr/bin/env python3

def digit2String(digit):
    """Converts an integer digit to its corresponding string
       representation.
    
    Parameter:
        digit: an integer in 0, 1, ..., 9
        
    Return value: 
        the corresponding character '0', '1', ..., '9'
        or None if a non-digit is passed as an argument
    """
    
    if (digit < 0) or (digit > 9):
        return None
    return chr(ord('0') + digit)
    
def letter2Index(letter):
    """Returns the position of a letter in the alphabet.
    
    Parameter:
        letter: an upper case or lower case letter
        
    Return value: the position of a letter in the alphabet
    """
    
    if (letter >= 'A') and (letter <= 'Z'):  # upper case
        return ord(letter) - ord('A') + 1
    if (letter >= 'a') and (letter <= 'z'):  # lower case
        return ord(letter) - ord('a') + 1
    return None                              # non-letter
    
