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
    
    tortoise.pencolor('black')
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    for segment in range(8):
        tortoise.forward(length)
        tortoise.left(135)
    tortoise.end_fill()

def stem(tortoise, length):
    tortoise.pencolor('green')
    tortoise.pensize(length / 20)
    tortoise.up()
    tortoise.forward(length / 2)
    tortoise.down()
    tortoise.right(90)
    tortoise.forward(length)

def flower(tortoise, fcolor, length):
    bloom(tortoise, fcolor, length)
    stem(tortoise, length)

def grow_flower(x, y):
    span = random.randrange(20, 200)
    fill = random.choice(['yellow', 'pink', 'red', 'purple'])
    tortoise = turtle.Turtle()
    tortoise.hideturtle()
    tortoise.speed(0)
    tortoise.up()
    tortoise.goto(x, y)
    tortoise.setheading(0)
    tortoise.pensize(1)
    tortoise.down()
    flower(tortoise, fill, span)

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

##george = turtle.Turtle()
##george.hideturtle()
##george.speed(0)
####flower(george, 'yellow', 200)
##
####flower(george, length=50, fcolor='orange')
####flower(george, 'purple', 350)
##
##screen = george.getscreen()
####screen.exitonclick()
##screen.onclick(grow_flower)
##screen.mainloop()




