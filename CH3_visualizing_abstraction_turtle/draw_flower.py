import turtle

george = turtle.Turtle()
george.hideturtle()
george.speed(6)

def turtle_200_135(t):
    """t : turtle object."""
    t.forward(200)
    t.left(135)

for i in range(8):
    turtle_200_135(george)

screen = george.getscreen()
screen.exitonclick()
    
