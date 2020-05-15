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
    tortoise.forward(length * 2)

def flower(tortoise, fcolor1, fcolor2, length, petals):
    bloom(tortoise, fcolor1, length, petals)
    tortoise.forward(length/4)
    tortoise.left(90)
    tortoise.up()
    tortoise.forward(length/9)
    tortoise.right(90)
    tortoise.down()
    bloom(tortoise, fcolor2, length/2, petals)
    stem(tortoise, length/2)



george = turtle.Turtle()
#george.hideturtle()
george.speed(2)

flower(george, fcolor1='yellow', fcolor2='red', length=200, petals=8)

screen = george.getscreen()

screen.mainloop()
