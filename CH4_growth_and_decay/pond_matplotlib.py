import matplotlib.pyplot as pyplot

def pond(years, init_pop, harvest):
    """Simulates a fish population in a fishing pond, and plots annual population
    size. Population grows 8% per year with an annual harvest.

    Args:
        years (int): The number of years to simulate
        init_pop (int): Initial population size
        harvest (int): Number of fish harvested annually

    Returns:
        Final population size after years years.
    """
    population = init_pop
    population_list = []
    population_list.append(init_pop)
    for year in range(years):
        population = 1.08 * population - harvest
        population_list.append(population)

    pyplot.plot(range(years + 1), population_list)
    pyplot.xlabel('Year')
    pyplot.ylabel('Fish Population Size')
    pyplot.show()
    
    
    return population

print(pond(5, 12000, 10))
