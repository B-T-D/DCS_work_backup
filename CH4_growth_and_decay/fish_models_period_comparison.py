
def annual(years, init_pop, harvest):
    population = init_pop
    for year in range(years):
        population = 1.08 * population - harvest
        print('{0:^4} | {1:>9.2f}'.format(year + 1, population))
    return population

def monthly(years, init_pop, harvest):
    population = init_pop
    for year in range(years):
        for month in range(12):
            population = population + (0.08 / 12) * population - (1500 / 12)
        print('{0:^4} | {1:>9.2f}'.format(year + 1, population))
    return population

print(annual(2, 12000, 1500))
print(monthly(2, 12000, 1500))
        
