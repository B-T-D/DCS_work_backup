import turtle
import random

def setup():
    """Returns a turtle object, t, configured usefully for this exercise."""
    t = turtle.Turtle()
    t.speed(0)
    screen = t.getscreen()
    screen.setup(width=1200, height=1000)
    return t

def random_walk(steps):
    t = setup()
    step_length = 15
    for step in range(steps):
        angle = random.randrange(360)
        t.setheading(angle)
        t.forward(step_length)

random_walk(1000)
