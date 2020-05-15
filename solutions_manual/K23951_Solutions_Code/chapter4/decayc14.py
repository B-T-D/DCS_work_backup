#!/usr/bin/env python3

import matplotlib.pyplot as pyplot

def decayC14(originalAmount, years, dt):
    """Approximates the continuous decay of carbon-14.
    
    Parameters:
        originalAmount: the original quantity of carbon-14 (g)
        years: number of years to simulate
        dt: the value of "Delta t" in the simulation
            (fraction of a year)
        
    Return value: 
        final quantity of carbon-14 (g)
    """
    
    k = -0.000121
    amount = originalAmount
    t = 0
    timeList = [0]                    # x values for plot
    amountList = [amount]             # y values for plot
    for step in range(1, int(years/dt) + 1):
        amount = amount + k * amount * dt
        t = step * dt
        timeList.append(t)
        amountList.append(amount)
    
    pyplot.plot(timeList, amountList)
    pyplot.xlabel('Years')
    pyplot.ylabel('Quantity of carbon-14')
    pyplot.show()
    
    return amount

decayC14(100, 20000, 0.01)
