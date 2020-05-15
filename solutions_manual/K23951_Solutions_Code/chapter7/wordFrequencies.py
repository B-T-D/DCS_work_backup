#!/usr/bin/env python3

import matplotlib.pyplot as pyplot

def getInputs():
    """Prompt for the name of a text file, a word to analyze, and a 
       window length.  Read and return the text, word, and window length.
       
    Parameters: none
    
    Return value: a text, word, and window length
    """
    
    fileName = input('Text file name: ')                # get file name
    
    textFile = open(fileName, 'r', encoding = 'utf-8')  # read file
    text = textFile.read()
    textFile.close()
    
    word = input('Word: ')                         # get word
    windowLength = int(input('Window length: '))   # get window length
    
    return text, word, windowLength

def count(text, target):
    """Count the number of target strings in text.
    
    Parameters:
        text: a string object
        target: a string object
        
    Return value: the number of times target occurs in text
    """
    
    count = 0
    for index in range(len(text) - len(target) + 1):
        if text[index:index + len(target)] == target:
            count = count + 1
    return count
    
def getWordCounts(text, word, windowLength):
    """Find the number of times word occurs in each window in the text.
       
    Parameters:
        text: a string containing a text
        word: a string
        windowLength: the integer length of the windows
        
    Return values: average count per window and list of window counts
    """

    wordCount = 0
    windowCount = 0
    wordCounts = []
    for index in range(0, len(text) - windowLength + 1, windowLength):
        window = text[index:index + windowLength]
        windowCount = windowCount + 1
        wordsInWindow = count(window, word)
        wordCount = wordCount + wordsInWindow
        wordCounts.append(wordsInWindow)
    
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
