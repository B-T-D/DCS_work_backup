import turtle

def draw_square(tortoise, width):
    for i in range(4):
        tortoise.forward(width)
        tortoise.left(90)
    
t = turtle.Turtle()
t.speed(5)

##draw_square(t, 400)

