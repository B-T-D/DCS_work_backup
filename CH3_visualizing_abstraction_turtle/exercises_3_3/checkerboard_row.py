import turtle

import square

def setup():
    """Returns a turtle object, t, configured usefully for this exercise."""
    t = turtle.Turtle()
    t.speed(6)
    screen = t.getscreen()
    screen.setup(width=1200, height=1000)
    return t

def draw_ckb_square(color):
    pass

def draw_row(tortoise, color1, color2):
    t = tortoise
    for i in range(int(8/2)):
        width = 50
        t.fillcolor(color1)
        t.begin_fill()
        square.draw_square(t, width)
        t.end_fill()
        t.forward(width)
        t.fillcolor(color2)
        t.begin_fill()
        square.draw_square(t, width)
        t.end_fill()
        t.forward(width)

def reposition(t, width):
    t.up()
    t.setheading(90)
    t.forward(width * 2)
    t.left(90)
    t.setheading(180)
    t.down()

def checkerboard(tortoise):
    t = tortoise
    width = 50
    for i in range(8):
        # Draw a row
        draw_row(t, 'red', 'black')
        reposition(t, width)

        

tortoise = setup()

##draw_row(tortoise, 'red', 'black')
##tortoise.setheading(90)
checkerboard(tortoise)
