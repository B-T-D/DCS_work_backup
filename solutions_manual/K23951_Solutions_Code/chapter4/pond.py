#!/usr/bin/env python3
    
def pond(years, initialPopulation, harvest):
    """Simulates a fish population in a fishing pond, and 
       prints annual population size.  The population 
       grows 8% per year with an annual harvest of 1500.
    
    Parameter:
        years: number of years to simulate
        
    Return value: the final population size
    """
    
    population = initialPopulation
    print('Year | Population')
    print('-----|-----------')
    for year in range(years):
        population = 1.08 * population - harvest
        print('{0:^4} | {1:>9.2f}'.format(year + 1, population))
        
    return population
    
def main():
    finalPopulation = pond(15, 12000, 800)
    print('The final population is', finalPopulation)
    
main()
