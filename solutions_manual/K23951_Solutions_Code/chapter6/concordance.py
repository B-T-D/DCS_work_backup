#!/usr/bin/env python3

def concordanceEntry(fileName, word):
    """Print all lines in a file containing the given word.
    
    Parameters:
        fileName: the name of the text file as a string
        word: the word to search for
        
    Return value: None
    """
    
    text = open(fileName, 'r', encoding = 'utf-8')
    lineCount = 1
    for line in text:
        found = find(line, word)
        if found >= 0:             # found the word in line
            space = ' ' * (80 - len(word) - found)
            print('{0:<6}'.format(lineCount) + space + line.rstrip())
        lineCount = lineCount + 1
    text.close()
