#!/usr/bin/env python3

import turtle

def koch(tortoise, length, depth):
    """Recursively draw a Koch curve.
    
    Parameters:
        tortoise: a Turtle object
        length: the length of a line segment
        depth: the desired depth of recursion
        
    Return value: None
    """
    
    if depth == 0:                             # base case
        tortoise.forward(length)
    else:                                      # recursive case
        koch(tortoise, length / 3, depth - 1)
        tortoise.left(60)
        koch(tortoise, length / 3, depth - 1)
        tortoise.right(120)
        koch(tortoise, length / 3, depth - 1)
        tortoise.left(60)
        koch(tortoise, length / 3, depth - 1)

def main():
    george = turtle.Turtle()
    koch(george, 400, 3)
    screen = george.getscreen()
    screen.exitonclick()

main()
