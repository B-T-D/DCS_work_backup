def pond(years, init_pop, harvest, dt):
    """
    Args:
        dt (float): Delta time. The size of the "update interval", as a
            proportion of a year. E.g. 1/12 for monthly update (proportional
            harvest and reproduction model numbers update 12 times per year). 
    """
    population = init_pop
    for step in range(1, int(years / dt) + 1):
        population = population + (0.08 * population - harvest) * dt
    return population
