import turtle

def draw_circle(tortoise, radius=50):
    """Draws the specific circle for this exercise, i.e. extent of 360."""
    tortoise.circle(radius, 360)

def start_pos_left(tortoise):
    tortoise.up()
    tortoise.setheading(180)
    tortoise.forward(9*50)
    tortoise.setheading(0)
    tortoise.down()

def start_pos_next_circle(tortoise, radius):
    tortoise.up()
    tortoise.setheading(0)
    tortoise.forward(2 * radius)
    tortoise.down()

def draw_horizontal_circles(tortoise, num_circles, radius):
    start_pos_left(tortoise)
    for i in range(num_circles):
        draw_circle(tortoise)
        start_pos_next_circle(tortoise, radius)
        

radius = 50
num_circles = 10
t = turtle.Turtle()
t.speed(6)


screen = t.getscreen()
screen.setup(width=1200)


draw_horizontal_circles(t, num_circles, radius)

