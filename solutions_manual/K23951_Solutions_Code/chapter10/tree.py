#!/usr/bin/env python3

import turtle

def tree(tortoise, length, depth):
    """Recursively draw a tree.
    
    Parameters:
        tortoise: a Turtle object
        length: the length of the trunk
        depth: the desired depth of recursion
        
    Return value: None
    """
    
    if depth <= 1:                   # the base case
        tortoise.forward(length)
        tortoise.backward(length)
    else:                            # the recursive case
        tortoise.forward(length)
        tortoise.left(30)
        tree(tortoise, length * (2 / 3), depth - 1)  
        tortoise.right(60)
        tree(tortoise, length * (2 / 3), depth - 1)  
        tortoise.left(30)
        tortoise.backward(length)

def main():
    george = turtle.Turtle()
    george.left(90)
    tree(george, 100, 4)
    screen = george.getscreen()
    screen.exitonclick()

main()
