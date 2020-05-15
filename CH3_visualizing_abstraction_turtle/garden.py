import turtle
import random

def grow_flower(x, y):
    span = random.randrange(20, 200)
    fill = random.choice(['yellow', 'pink', 'red', 'purple'])
    tortoise = turtle.Turtle()
    tortoise.hideturtle()
    tortoise.speed(6)
    tortoise.up()
    tortoise.goto(x, y)
    tortoise.setheading(0)
    tortoise.pensize(1)
    tortoise.down()
    flower(tortoise, fill, span)
