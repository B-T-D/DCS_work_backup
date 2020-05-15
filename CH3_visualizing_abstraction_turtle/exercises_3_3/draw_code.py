import turtle

t = turtle.Turtle()
t.speed(0)
size = 100

def draw_c():
    t.circle(size/2, -180)
    t.up()
    t.left(90)
    t.forward(size)

def draw_o():
    t.circle(size/2)

def draw_d():
    t.setheading(90)
    t.forward(size)
    t.setheading(0)
    t.circle(-size/2, 180)

def draw_e():
    t.setheading(90)
    t.forward(size)
    t.setheading(0)
    t.forward(size/2)
    t.setheading(270)
    t.up()
    t.forward(size/2)
    t.down()
    t.setheading(180)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size/2)
    t.setheading(0)
    t.forward(size/2)


def space():
    t.up()
    t.setheading(0)
    t.forward(size)
    t.down()

draw_c()
space()
draw_o()
space()
draw_d()
space()
draw_e()
