import matplotlib.pyplot as pyplot

def compete(pop1, pop2, birth1, birth2, death1, death2, years, dt):
    """
    Plots the values for simulated indirect, exploitative competition between two
    predator species.

    Args:
        pop1 (int): Starting population of first predator species.
        pop2 (int): Starting population of second predator species.
        birth1 (float): Birth rate proportional constant for first species
        birth2 (float): Birth rate proportional constant for second species
        death1 (float): Death rate proportional constant for first species
        death2 (float): Death rate proportional constant for second species
        years (int): Number of years to simulate.
        dt (float): The value of "delta t" in the simulation (fraction of a year)

    Returns:
        None
    """
    pop1_list = [pop1]
    pop2_list = [pop2]
    time_list = [0]
    for step in range(1, int(years / dt) + 1):
        # First compute the delta in each population's size, from end prior iteration
            # "delta species 'P'", i.e. pop1 species:
        dP = (birth1 * pop1) * dt - (death1 * pop1 * pop2) * dt # births minus deaths
            # "delta species 'Q'", i.e. pop2 species:
        dQ = (birth2 * pop2) * dt - (death2 * pop1 * pop2) * dt # births minus deaths

        # Then use those delta values to update each population's size
        pop1 = pop1 + dP
        pop2 = pop2 + dQ
        pop1_list.append(pop1)
        pop2_list.append(pop2)
        t = step * dt
        time_list.append(t)

    # pyplot calls
    pyplot.plot(time_list, pop1_list, label='Species 1 (aka P)')
    pyplot.plot(time_list, pop2_list, label='Species 2 (aka Q)')
    pyplot.legend()
    pyplot.xlabel('Years')
    pyplot.ylabel('Individuals')
    pyplot.show()

def sol_man(pop1, pop2, birth1, birth2, death1, death2, years, dt):
    pop1_list = [pop1]
    pop2_list = [pop2]
    time_list = [0]

    for step in range(1, int(years / dt) + 1):
        t = step * dt
        newPop1 = (birth1 * pop1 - death1 * pop1 * pop2) * dt
        newPop2 = (birth2 * pop2 - death2 * pop2 * pop1) * dt
        pop1 = pop1 + newPop1
        pop2 = pop2 + newPop2

        time_list.append(t)
        pop1_list.append(pop1)
        pop2_list.append(pop2)
            


    # pyplot calls
    pyplot.plot(time_list, pop1_list, label='Species 1 (aka P)')
    pyplot.plot(time_list, pop2_list, label='Species 2 (aka Q)')
    pyplot.legend()
    pyplot.xlabel('Years')
    pyplot.ylabel('Individuals')
    pyplot.show()

pop1 = 21
pop2 = 26
birth1 = 1.0
death1 = 0.2
birth2 = 1.02
death2 = 0.25
years = 6
dt = 0.001
compete(pop1, pop2, birth1, birth2, death1, death2, years, dt)
sol_man(pop1, pop2, birth1, birth2, death1, death2, years, dt)

    
