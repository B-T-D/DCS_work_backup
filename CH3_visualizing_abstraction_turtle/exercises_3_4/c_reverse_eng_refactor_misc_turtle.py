"""
Exercise 3.4.3
Date: 2020-03-28 19:03

"""

import turtle

def draw_outer_semicircle(tortoise):
    """Draws the red, larger outer semi circle component.

    Args:
        tortoise (Turtle): Turtle object with which to draw the outer semicircle.
    
    Returns:
        None
    """

    tortoise.setposition(0, 100)
    tortoise.pencolor('red')
    tortoise.fillcolor('red')
    tortoise.begin_fill()
    tortoise.circle(-100, 180) # Draw the semicircle with the flat side facing left
    tortoise.right(90)
    tortoise.forward(200)
    tortoise.end_fill()

def reposition(tortoise):
    """Repositions the tortoise to the inner-semicircle start location.

    Args:
        tortoise (Turtle): Turtle object used for drawing the outer semicircle
            and which is to be used to draw the inner semicircle.

    Returns:
        None
    """
    
    tortoise.up()
    tortoise.right(90)
    tortoise.forward(25)
    tortoise.right(90)
    tortoise.forward(50)
    tortoise.left(90)
    tortoise.down()

def draw_inner_semicircle(tortoise):
    """Draws the inner, smaller, white semicircle component.

    Args:
        tortoise (Turtle): Turtle object positioned at the inner-semicircle
            start position.

    Returns:
        None
    """

    tortoise.pencolor('white')
    tortoise.fillcolor('white')
    tortoise.begin_fill()
    tortoise.circle(-50, 180)
    tortoise.right(90)
    tortoise.forward(100)
    tortoise.end_fill()

    # TODO further refactor by creating a draw_d(extent, fillcolor) function
    #   to reduce repeated code in outer an inner semicircle functions. 

def draw_big_red_d(tortoise):
    """Draws the large red 'D'-shaped graphic.

    Args:
        tortoise (Turtle): Turtle object with which to draw the shape.

    Returns:
        None
    """
    
    draw_outer_semicircle(tortoise)
    reposition(tortoise)
    draw_inner_semicircle(tortoise)

def main():
    """Draws a red semi circle with a second, smaller white semi-circle inside
    it, such that the final drawing resembles a red capital letter 'D'. Waits
    for a mouse click to exit. 
    """

    george = turtle.Turtle()
    draw_big_red_d(george)
    screen = george.getscreen()
    screen.exitonclick()

main()
    
