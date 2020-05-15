#!/usr/bin/env python3

import matplotlib.pyplot as pyplot
import random

def sumRandom(n):
    """Returns the sum of n pseudorandom numbers in [0,1).
    
    Parameter:
        n: the number of pseudorandom numbers to generate
        
    Return value: the sum of n pseudorandom numbers in [0,1)
    """
    
    sum = 0
    for index in range(n):
        sum = sum + random.random()
    return sum
    
def sumRandomHist(n, trials):
    """Displays a histogram of sums of n pseudorandom numbers.
    
    Parameters:
        n: the number of pseudorandom numbers in each sum
        trials: the number of sums to generate
        
    Return value: None
    """
    
    samples = [ ]
    for index in range(trials):
        samples.append(sumRandom(n))
    pyplot.hist(samples, 100)
    pyplot.show()
    
def main():
    sumRandomHist(10, 100000)
    
main()
