#!/usr/bin/env python3

def wordCount5(text):
    """Count the number of words in a string.
    
    Parameter:
        text: a string object
        
    Return value: the number of words in text 
    """
    
    count = 0
    prevCharacter = ' '
    for character in text:
        if character in ' \t\n' and prevCharacter not in ' \t\n':
            count = count + 1
        prevCharacter = character
    if prevCharacter not in ' \t\n':
        count = count + 1
    return count

def wcFile(fileName):
    """Return the number of words in the file with the given name.
    
    Parameter:
        fileName: the name of a text file
        
    Return value: the number of words in the file
    """
    
    textFile = open(fileName, 'r', encoding = 'utf-8')
    text = textFile.read()
    textFile.close()
    
    return wordCount5(text)
    
