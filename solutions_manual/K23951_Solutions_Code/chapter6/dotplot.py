#!/usr/bin/env python3

import matplotlib.pyplot as pyplot

def dotplot(text1, text2):
    """Display a dot plot comparing two strings.
    
    Parameters:
        text1: a string object
        text2: a string object
        
    Return value: None
    """
    
    text1 = text1.lower()
    text2 = text2.lower()
    x = []
    y = []
    for index in range(len(text1)):
        for index2 in range(len(text2)):
            if text1[index] == text2[index2]:
                x.append(index)
                y.append(index2)
    pyplot.scatter(x, y)
    pyplot.xlim(0, len(text1))
    pyplot.ylim(0, len(text2))
    pyplot.xlabel(text1)
    pyplot.ylabel(text2)
    pyplot.show()

