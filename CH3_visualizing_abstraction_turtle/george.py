import turtle


george = turtle.Turtle()
george.hideturtle()
george.speed(6)
##george.pencolor('red')

screen = george.getscreen()
screen.colormode(255)


george.pencolor((127, 0, 127))
george.fillcolor('yellow')
george.begin_fill()

for segment in range(8):
    george.forward(200)
    george.left(135)

george.end_fill()

screen.exitonclick()
    
