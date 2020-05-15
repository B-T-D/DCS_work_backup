import turtle

##import petals_funcs as pf

def bloom(tortoise, fcolor, length, petals):
    tortoise.pencolor('black')
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    for segment in range(petals):
        tortoise.forward(length)
##        tortoise.left(pf.degrees(petals))
        tortoise.left(1080/petals)
    tortoise.end_fill()

def stem(tortoise, length):
    tortoise.pencolor('green')
    tortoise.pensize(length / 20)
    tortoise.up()
    tortoise.forward(length / 2)
    tortoise.down()
    tortoise.right(90)
    tortoise.forward(length)

def flower(tortoise, fcolor, length, petals):
    bloom(tortoise, fcolor, length, petals)
    stem(tortoise, length)



george = turtle.Turtle()
#george.hideturtle()
george.speed(6)

flower(george, fcolor='purple', length=200, petals=5)

screen = george.getscreen()

screen.mainloop()
