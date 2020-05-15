import matplotlib.pyplot as pyplot

def SIR(population, days, dt):
    """Simulates the SIR model of infectious disease and 
       plots the population sizes over time.
    
    Parameters:
        population: the population size
        days: number of days to simulate
        dt: the value of "Delta t" in the simulation
            (fraction of a day)
        
    Return value: None
    """
    
    susceptible = population - 1  # susceptible count = S(t)
    infected = 1.0                # infected count = I(t)
    recovered = 0.0               # recovered count = R(t)
    recRate = 0.25                # recovery rate r
    infRate = 0.0004              # infection rate d
##    infRate = 0.0002 # simulating vaccinations, exercise 4.4.7
    SList = [susceptible]
    IList = [infected]
    RList = [recovered]
    timeList = [0]
	
    # Loop using the difference equations goes here.
    for step in range(1, int(days/dt) + 1):
        # First compute the change in each population's size based on the
        #   population sizes from the previous iteration.
        new_recovered = recRate * infected * dt
        new_susceptible = infRate * susceptible * infected * dt
        new_infected = new_susceptible - new_recovered

        # Then use those values to update the new population sizes
        recovered = recovered + new_recovered
        susceptible = susceptible - new_susceptible
        infected = infected + new_infected
        RList.append(recovered)
        SList.append(susceptible)
        IList.append(infected)
        t = step * dt
        timeList.append(t)

    # pyplot calls
    pyplot.plot(timeList, SList, label = 'Susceptible')
    pyplot.plot(timeList, IList, label = 'Infected')
    pyplot.plot(timeList, RList, label = 'Recovered')
    pyplot.legend(loc = 'center right')
    pyplot.xlabel('Days')
    pyplot.ylabel('Individuals')
    pyplot.show()

##SIR(2200, 30, 0.01)
SIR(2200, 90, 0.01)
