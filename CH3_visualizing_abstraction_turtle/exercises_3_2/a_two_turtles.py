import turtle

red = turtle.Turtle()
blue = turtle.Turtle()

# Don't want to hideturtle() for either, picture at 3.1 that we're trying to
    # copy has the arrows on the ends of the lines.

red.pencolor('red')
blue.pencolor('blue')

blue.forward(100)
blue.left(45)
blue.forward(100)

red.left(120)
red.forward(100)
red.left(90)
red.forward(50)

