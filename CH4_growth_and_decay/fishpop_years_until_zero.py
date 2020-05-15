def years_until_zero(init_pop, harvest):
    """Computes number of years until fish population reaches zero.
    For a population that grows 8% per year before the annual harvest."""

    population = init_pop
    year = 0
    while population > 0:
        population = 1.08 * population - harvest
        year += 1
        if year > 1000:
            print("Fish won't deplete for over 1000 years.")
            break
    return year

print(years_until_zero(0, 10))
