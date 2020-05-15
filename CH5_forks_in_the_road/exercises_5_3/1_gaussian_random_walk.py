import turtle
import random
import math
import time
import matplotlib.pyplot as pyplot

def random_walk(steps, tortoise, draw):
    """Displays a random walk on a grid.

    Args:
        steps (int): Number of steps in the random walk
        tortoise : A Turtle object

    Returns:
        (int): Final distance from the origin.
    """

    x = 0 # Initialize (x, y) = (0, 0)
    y = 0
    move_length = 10 # length of a turtle step

    for step in range(steps):
        x = x + random.gauss(0, 0.5)
        y = x + random.gauss(0, 0.5)
        if draw:
            tortoise.goto(x * move_length, y * move_length)
    
    return math.sqrt(x * x  + y * y) # return distance from (0, 0)

def rw_monte_carlo(steps, trials):
    """A Monte Carlo simulation to find the expected distance that a random
    walk finishes from the origin.

    Args:
        steps (int): Number of steps in the random walk
        trials (int): Number of random walks.

    Returns:
        (float): Average distance from the origin.
    """
    total_distance = 0
    for trial in range(trials):
        distance = random_walk(steps, None, False)
        total_distance = total_distance + distance
    return total_distance / trials

def plot_distances(max_steps, trials):
    """
    Plots the average distances traveled by random walks of 100, 200, ...,
    max_steps unit-length steps.

    Args:
        max_steps (int): Maximum number of steps for the plot
        trials (int): Number of random walks in each simulation

    Returns:
        None
    """
    print(f"Running plot_distances({max_steps}, {trials})")
    distances = []
    step_range = range(100, max_steps + 1, 100)
    y = []
    for steps in step_range:
        distance = rw_monte_carlo(steps, trials)
        distances.append(distance)
        y.append(math.sqrt(steps))

    pyplot.plot(step_range, y, label='Model Function') # Plot sqrt(n), the model function
    pyplot.plot(step_range, distances, label = 'Simulation')
    pyplot.legend(loc = 'center right')
    pyplot.xlabel('Number of Steps')
    pyplot.ylabel('Distance From Origin')
    pyplot.show()

def rw_histogram(steps, trials):
    """Draws a histogram of the given number of trials of a random walk
    with the given number of steps.

    Args:
        steps (int): Number of steps in the random walk
        trials (int): Number of random walks

    Returns:
        None
    """

    distances = []
    for trial in range(trials):
        distance = random_walk(steps, None, False)
        distances.append(distance)

##    pyplot.hist(distances, 75)
    pyplot.hist(distances, 500)
    pyplot.show()

##random_walk(1000, turtle.Turtle(), draw=True)
##rw_histogram(1000, 10000)
plot_distances(1000, 1000)
