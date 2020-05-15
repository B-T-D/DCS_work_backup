#!/usr/bin/env python3

import random
import math
import matplotlib.pyplot as pyplot

def randomWalk(steps, tortoise, draw):
    """Displays a random walk on a grid.
    
    Parameters:
        steps: the number of steps in the random walk
        tortoise: a Turtle object
        
    Return value: the final distance from the origin
    """
    
    x = 0                      # initialize (x, y) = (0, 0)
    y = 0
    moveLength = 10            # length of a turtle step
    for step in range(steps):
        r = random.random()    # randomly choose a direction
        if r < 0.25:    # if r < 0.25,
            x = x + 1   #    move to the east and finish
        elif r < 0.5:   # otherwise, if r is in [0.25, 0.5),
            y = y + 1   #    move to the north and finish
        elif r < 0.75:  # otherwise, if r is in [0.5, 0.75),
            x = x - 1   #    move to the west and finish
        else:           # otherwise,
            y = y - 1   #    move to the south and finish
            
        if draw:
            tortoise.goto(x * moveLength, y * moveLength)  # draw one step
        
    return math.sqrt(x * x + y * y)  # return distance from (0, 0)
    
def rwMonteCarlo(steps, trials):
    """A Monte Carlo simulation to find the expected distance
       that a random walk finishes from the origin.
    
    Parameters:
        steps: the number of steps in the random walk
        trials: the number of random walks
        
    Return value: the average distance from the origin
    """
    
    totalDistance = 0
    for trial in range(trials):
        distance = randomWalk(steps, None, False)
        totalDistance = totalDistance + distance
    return totalDistance / trials

def plotDistances(maxSteps, trials):
    """Plots the average distances traveled by random walks of
       100, 200, ..., maxSteps steps.
    
    Parameters:
        maxSteps: the maximum number of steps for the plot
        trials: the number of random walks in each simulation
        
    Return value: None
    """
    
    distances = [ ]
    y = [ ]
    stepRange = range(100, maxSteps + 1, 100)
    for steps in stepRange:
        distance = rwMonteCarlo(steps, trials)
        distances.append(distance)
        y.append(math.sqrt(steps))
        
    pyplot.plot(stepRange, distances, label = 'Simulation')
    pyplot.plot(stepRange, y, label = 'Model Function')
    pyplot.legend(loc = 'center right')
    pyplot.xlabel('Number of Steps')
    pyplot.ylabel('Distance From Origin')
    pyplot.show()
    
def rwHistogram(steps, trials):
    """Draw a histogram of the given number of trials of
       a random walk with the given number of steps.
    
    Parameters:
        steps: the number of steps in the random walk
        trials: the number of random walks
        
    Return value: None
    """
    
    distances = [ ]
    for trial in range(trials):
        distance = randomWalk(steps, None, False)
        distances.append(distance)
    
    pyplot.hist(distances, 75)
    pyplot.show()

def main():
    rwHistogram(1000, 5000)
    plotDistances(1000, 5000)
    
main()
