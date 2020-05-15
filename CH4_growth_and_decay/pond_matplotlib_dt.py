import matplotlib.pyplot as pyplot

def pond(years, init_pop, harvest, dt):
    """Simulates a fish population in a fishing pond, and plots annual population
    size. Population grows 8% per year with an annual harvest.

    Args:
        years (int): The number of years to simulate
        init_pop (int): Initial population size
        harvest (int): Number of fish harvested annually
        dt (float): Delta time. The size of the "update interval", as a
            proportion of a year. E.g. 1/12 for monthly update (proportional
            harvest and reproduction model numbers update 12 times per year).

    Returns:
        Final population size after years years.
    """
    population = init_pop
    population_list = [init_pop]
    time_list = [0]
    t = 0
    for step in range(1, int(years / dt) + 1):
        population = population + (0.08 * population - harvest) * dt
        population_list.append(population)
        t = step * dt
        time_list.append(t)

    pyplot.plot(time_list, population_list)
    pyplot.xlabel('Year')
    pyplot.ylabel('Fish Population Size')
    pyplot.show()
    
    
    return population

print(pond(15, 12000, 1500, 0.01))
