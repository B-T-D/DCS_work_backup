#!/usr/bin/env python3

def find(text, target):
    """Find the index of the first occurrence of target in text.
    
    Parameters:
        text: a string object to search in
        target: a string object to search for
        
    Return value: the index of the first occurrence of target in text
    """
    
    for index in range(len(text) - len(target) + 1):
        if text[index:index + len(target)] == target:
            return index
    return -1

def main():
    textFile = open('mobydick.txt', 'r', encoding = 'utf-8')
    text = textFile.read()
    textFile.close()

    word = input('Search for: ')
    while word != 'q':
        index = find(text, word)
        print(word, 'first appears at position', index)
        word = input('Search for: ')

main()
