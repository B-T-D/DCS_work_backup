import turtle

def setup():
    """Returns a turtle object, t, configured usefully for this exercise."""
    t = turtle.Turtle()
    t.speed(9)
    screen = t.getscreen()
    screen.setup(width=1200, height=1000)
    return t

def start_pos(t, radius=50):
    """Positions the tortoise pen in the upper left of the window."""
    t.up()
    t.goto(-550, 400)
    t.circle(radius, 225)
    t.down()
    
def arc(t, opening, radius=50):
    if opening == True:
        radius = -radius
    t.circle(radius, 180)

def draw_diagonal_circles(t, num_circles, radius):
    t.pencolor('red')
    opening = False
    for i in range(num_circles):
        arc(t, opening)
        opening = not(opening)
    t.pencolor('blue')
    opening = True if num_circles % 2 == 0 else False
    for i in range(num_circles):
        arc(t, opening)
        opening = not(opening)
    
def diagonal_circles(tortoise):
    t = tortoise
    start_pos(t)
    draw_diagonal_circles(t, num_circles=10, radius=50)

tortoise = setup()
diagonal_circles(tortoise)

