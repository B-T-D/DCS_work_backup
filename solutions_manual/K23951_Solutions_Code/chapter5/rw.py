#!/usr/bin/env python3

import random
import math
import turtle

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

def main():
    george = turtle.Turtle()
    distance = randomWalk(1000, george, True)
    print(distance)
    screen = george.getscreen()
    screen.exitonclick()
    
main()
