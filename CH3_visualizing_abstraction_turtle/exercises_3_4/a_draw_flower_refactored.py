"""
Purpose: Draw a flower
Author: Ben
Date: March 28, 2020
"""

import turtle
import random

def bloom(tortoise, fcolor, length):

    """Draws a geometric flower bloom.

    Args:
        tortoise (Turtle object): Turtle object with which to draw the bloom.
        fcolor (str): A color string to use to fill in the bloom.
        length (int): The length of each segment of the bloom.

    Returns:
        None
    """
    
    tortoise.pencolor('black') # set tortoise's pen color to black
    tortoise.fillcolor(fcolor) # and fill color to fcolor
    tortoise.begin_fill()
    for segment in range(8): # draw an 8-sided
        tortoise.forward(length) #  geometric flower bloom
        tortoise.left(135)
    tortoise.end_fill()

def stem(tortoise, length):
    """Draws a flower stem.

    Args:
        tortoise (Turtle object): a Turtle object, located at the bloom starting position.
        length (int): The length of the stem and each segment of the bloom.

    Returns:
        None
    """
    tortoise.pencolor('green') # Draw the stem as green
    tortoise.pensize(length / 20) # Draw the stem thicker than the petal borders
    tortoise.up() # Reposition tortoise from where it ended drawing the bloom
    tortoise.forward(length / 2) #  to bottom-center of bloom
    tortoise.down() #   from where it will start drawing the stem
    tortoise.right(90) # Stem extends straight down
    tortoise.forward(length)

def flower(tortoise, fcolor, length):
    """Draws a flower.

    Args:
        tortoise (Turtle): A Turtle object with which to draw the flower.
        fcolor (str): A fill-color string to use to fill the bloom.
        length (int): The length of each segment of the bloom.
    
    Returns:
        None
    
    """
    bloom(tortoise, fcolor, length) # Draw the bloom
    stem(tortoise, length) # and then the stem.


def main():
    """Draws a yellow flower with segment length 200, and waits for a mouse
    click to exit."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(6)
    flower(t, 'yellow', 200)
    screen = t.getscreen()
    screen.exitonclick()

main()
