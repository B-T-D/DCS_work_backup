#!/usr/bin/env python3

import matplotlib.pyplot as pyplot

def pond(years, initialPopulation, harvest, dt):
    """Simulates a fish population in a fishing pond, and 
       plots annual population size.  The population 
       grows at a nominal annual rate of 8% 
       with an annual harvest.
    
    Parameters:
        years: number of years to simulate
        initialPopulation: the initial population size
        harvest: the size of the annual harvest
        dt: the value of "Delta t" in the simulation
            (fraction of a year)
        
    Return value: the final population size
    """
    
    population = initialPopulation
    populationList = [initialPopulation]
    timeList = [0]
    t = 0
    for step in range(1, int(years / dt) + 1):
        population = population + (0.08 * population - harvest) * dt
        populationList.append(population)
        t = step * dt
        timeList.append(t)
        
    pyplot.plot(timeList, populationList)
    pyplot.xlabel('Year')
    pyplot.ylabel('Fish Population Size')
    pyplot.show()
    
    return population

pond(20, 12000, 1500, 0.01)
