#!/usr/bin/env python3

def wordCount1(text):
    """Approximate the number of words in a string by counting 
       the number of spaces, tabs, and newlines.
    
    Parameter:
        text: a string object
        
    Return value: the number of spaces, tabs and newlines in text 
    """
    
    return text.count(' ') + text.count('\t') + text.count('\n')
    
def wordCount2(text):        
    """ (docstring omitted) """
    
    return text.count(' ') - text.count('  ') + 1

def wordCount3(text):
    """ (docstring omitted) """
    
    count = 0
    for character in text:
        if character == ' ' or character == '\t' or character == '\n':
            count = count + 1
    return count
    
def wordCount4(text):
    """ (docstring omitted) """
    
    count = 0
    prevCharacter = ' '
    for character in text:
        if character in ' \t\n' and prevCharacter not in ' \t\n':
            count = count + 1
        prevCharacter = character
    return count
    
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
    
def main():
    shortText = 'This is not long.  But it will do. \n' + \
                'All we need is a few sentences.'
    wc = wordCount5(shortText)
    print(wc)
    
main()