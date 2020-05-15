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
        r = random.random() # randomly choose a direction
        if r < 0.25:
            x = x + 1 # move to the east and finish
        elif r < 0.40:
            y = y + 1 # move to the north and finish
        elif r < 0.65:
            x = x - 1 # move to the west and finish
        else: # 1.00 - 0.65 = 0.35
            y = y - 1 # move to the south and finish
        if draw:
            tortoise.goto(x * move_length, y * move_length) # Draw one step

    return math.sqrt(x * x  + y * y) # return distance from (0, 0)

random_walk(500, turtle.Turtle(), True)
