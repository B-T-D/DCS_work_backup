# Difference equation is
#   R(m) = R(m - 1) + R(m - 2)
#   Each female rabbit takes 1 month to reach sexual maturity, hence R(m - 2).
#   Each breeding female rabbit has 2 babies per month, one male, one female.
#       So the monthly proportional increase in female pop is 1 * (number of females that are at least 2 months old).

import matplotlib.pyplot as pyplot

def female_rabbits(months):
    """
    """
    fem_pop_init = 1 # Starts with one female
    fem_pop_list = [fem_pop_init]
    months_list = [0]
    fem_pop = fem_pop_init
    prior_fem_pop = 0
    for month in range(1, months + 1):
        fem_pop = fem_pop + prior_fem_pop
        fem_pop_list.append(fem_pop)
        months_list.append(month)
        prior_fem_pop = fem_pop_list[month - 1]

    pyplot.plot(months_list, fem_pop_list)
    pyplot.xlabel('Month')
    pyplot.ylabel('Female rabbits')
    pyplot.show()

    return fem_pop

def sol_man(months):
    population2 = 0 # R(m-2)
    population1 = 1 # R(m-1)
    population_list = [1]
    for month in range(1, months + 1):
        population = population1 + population2 # R(m)
        population2 = population1
        population1 = population
        population_list.append(population)
    pyplot.plot(range(months + 1), population_list)
    pyplot.xlabel('Month')
    pyplot.ylabel('Rabbit Population Size')
    pyplot.show()
    return population

female_rabbits(10)
sol_man(10)


##for i in range(11):
##    print("{} | {}".format(i, female_rabbits(i)))
        
