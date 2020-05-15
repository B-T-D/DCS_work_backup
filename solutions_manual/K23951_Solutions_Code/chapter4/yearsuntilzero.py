#!/usr/bin/env python3

def yearsUntilZero(initialPopulation, harvest):
    """Computes # of years until a fish population reaches zero.
       Population grows 8% per year with an annual harvest.
    
    Parameters:
        initialPopulation: the initial population size
        harvest: the size of the annual harvest
        
    Return value: year during which the population reaches zero
    """
    
    population = initialPopulation
    year = 0
    while population > 0:
        population = 1.08 * population - harvest
        year = year + 1
    return year
