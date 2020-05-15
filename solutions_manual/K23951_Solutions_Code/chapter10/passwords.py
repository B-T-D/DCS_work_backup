#!/usr/bin/env python3

def passwords(length, characters):
    """Return a list of all possible passwords with the given length,
       using the given characters.

    Parameters:
        length: the length of the passwords
        characters: a string containing the characters to use

    Return value: 
        a list of all possible passwords with the given length,
        using the given characters
    """

    if length == 0:
        return ['']
    
    shorter = passwords(length - 1, characters)
    
    passwordList = []
    for character in characters:
        for shorterPassword in shorter:
            passwordList.append(character + shorterPassword)
        
    return passwordList
