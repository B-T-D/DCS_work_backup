#!/usr/bin/env python3

import matplotlib.pyplot as pyplot

def getInputs():
    """Prompt for the name of a text file, a word to analyze,
       and a window length.  Read and return the text in the file
       and the word and window length.
       
    Parameters: none
    
    Return value: a text, word, and window length
    """
    
    fileName = input('Text file name: ')
    
    textFile = open(fileName, 'r', encoding = 'utf-8')
    text = textFile.read()
    textFile.close()
    
    word = input('Word: ')
    windowLength = int(input('Window length: '))
    
    return text, word, windowLength

def count(text, target):
    """Count the number of target strings in text.
    
    Precondition: text and target are string objects
        
    Postcondition: returns number of occurrences of target in text
    """
    
    assert isinstance(text, str) and isinstance(target, str), \
           'arguments must be strings'
    
    count = 0
    for index in range(len(text) - len(target) + 1):
        if text[index:index + len(target)] == target:
            count = count + 1
    return count
    
def getWordCounts(text, word, windowLength):
    """Find the number of times word occurs in each window in the text.

    Precondition: text and word are string objects and
                  windowLength is a positive integer and
                  text contains at least windowLength characters

    Postcondition: returns a list of word frequencies and the
                   average number of occurrences of word per window
    """

    assert isinstance(text, str) and isinstance(word, str), \
           'first two arguments must be strings'
           
    assert isinstance(windowLength, int) and windowLength > 0, \
           'window length must be a positive integer'
           
    assert len(text) >= windowLength, \
           'window length must be shorter than the text'
    
    wordCount = 0
    windowCount = 0
    wordCounts = []
    for index in range(0, len(text) - windowLength + 1, windowLength):
        window = text[index:index + windowLength]
        windowCount = windowCount + 1
        wordsInWindow = count(window, word)
        wordCount = wordCount + wordsInWindow
        wordCounts.append(wordsInWindow)
    
    assert windowCount > 0, 'no windows were found'
    
    return wordCount / windowCount, wordCounts

def plotWordCounts(wordCounts):
    """Plot a list of word frequencies.
    
    Parameter:
        wordCounts: a list of word frequencies
        
    Return value: None
    """
    
    numWindows = len(wordCounts)
    pyplot.plot(range(numWindows), wordCounts)
    pyplot.xlabel('Window number')
    pyplot.ylabel('Frequency')
    pyplot.xlim(-1, numWindows + 1)
    pyplot.ylim(0, max(wordCounts) + 1)
    pyplot.show()
    
def main():
    text, word, windowLength = getInputs()
    
    average, wordCounts = getWordCounts(text, word, windowLength)
    
    plotWordCounts(wordCounts)
    print(word, 'occurs on average', average, 'times per window.')

main()
