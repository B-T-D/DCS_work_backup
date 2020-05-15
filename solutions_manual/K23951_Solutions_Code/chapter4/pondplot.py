#!/usr/bin/env python3

import matplotlib.pyplot as pyplot

def pond(years, initialPopulation, harvest):
    """Simulates a fish population in a fishing pond, and 
       plots annual population size.  The population 
       grows 8% per year with an annual harvest.
    
    Parameters:
        years: number of years to simulate
        initialPopulation: the initial population size
        harvest: the size of the annual harvest
        
    Return value: the final population size
    """
    
    population = initialPopulation
    populationList = [ ]
    populationList.append(initialPopulation)
    for year in range(years):
        population = 1.08 * population - harvest
        populationList.append(population)
        
    pyplot.plot(range(years + 1), populationList)
    pyplot.xlabel('Year')
    pyplot.ylabel('Fish Population Size')
    pyplot.show()
    
    return population
