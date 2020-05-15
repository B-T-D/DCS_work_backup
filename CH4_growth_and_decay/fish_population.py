
def growth(population, years, rate, num_lost):
    for year in range(years):
        population = ( 1 + rate) * population - num_lost
    return population

def exhaustion_year(start_pop, growth_rate, harvest):
    """Returns the number of years until the fish population will be exhausted
    for a given population growth rate and annual harvest quantity."""

    fish_left = start_pop
    years_elapsed = 0
    while fish_left > 0:
        fish_left = growth(fish_left,
                           years=1,
                           rate=growth_rate,
                           num_lost = harvest)
        years_elapsed += 1
        if years_elapsed > 1000:
            break
    return years_elapsed

def max_sustainable_harvest(rate, start_pop):
    """Returns the largest number of fish that could be harvested annually
    without causing the population to shrink."""
    # The fish count will be stable if the number harvested equals the number
    #   of new fish created by population growth reproduction
    return rate * start_pop

def pond(years, init_pop, harvest):
    """(From the book, for purpose of demoing the strting formatting alignment characters)"""
    population = init_pop
    print('Year | Population')
    print('-----|----------')
    for year in range(years):
        population = 1.08 * population - harvest
        print('{0:^4} | {1:>9.2f}'.format(year + 1, population))
##        print(f'{(year + 1, 0:^4)} | {(population, 1:>9.2f)}')

population = 12000
years = 4
rate = 0.08
num_lost = 1500

print(growth(population, years, rate, num_lost))

# At a max harvest of 1500, when will the pond run out of fish?

years_elapsed = 0
fish_left = 12000
harvest = 1500

print(exhaustion_year(start_pop=12000, growth_rate=0.08, harvest=1500))

print(max_sustainable_harvest(0.08, 12000))

print(exhaustion_year(12000, 0.08, 959))


print(f"If we change the annual harvest to 800, there will be {growth(population, 15, 0.08, 800)} fish in the pond in 15 years.")
print(growth(population, 15, 0.08, 800))


print(f"If you harvested 960 fish per year, the exhaustion year would be {exhaustion_year(12000, 0.08, 960)}")


print("------")
print("pond func call:")
pond(years=15, init_pop=12000, harvest = 1500)
              
    
