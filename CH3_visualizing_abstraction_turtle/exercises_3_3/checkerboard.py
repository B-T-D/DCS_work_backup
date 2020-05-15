import turtle


def setup():
    """Returns a turtle object, t, configured usefully for this exercise."""
    t = turtle.Turtle()
    t.speed(2)
    screen = t.getscreen()
    screen.setup(width=1200, height=1000)
    return t

def draw_ckb_square(t, color, width=50):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()
    next_square(t)

def next_square(t, width=50):
    t.up()
    t.left(90)
    t.forward(width)
    t.down()
    
##def draw_row(tortoise, color1, color2, row_num):
##    t = tortoise
##    width = 50
##    for i in range(int(8/2)):
##        draw_ckb_square(t, color1)
##        draw_ckb_square(t, color2)
##    next_row(t, row_num)

def next_row(t, row_num, width=50):
    t.up()
##    if row_num % 2 != 0:
##        t.goto(t.xcor(), t.ycor() + 2 * width)
##        t.setheading(180)
##    if row_num % 2 == 0:
##        t.goto(t.xcor(), t.ycor() + width)
##        t.setheading(0)
    t.down()
    
##def checkerboard(tortoise):
##    t = tortoise
##    width = 50
##    num_rows = 1
##    row_num = 1
##    for i in range(num_rows):
##        draw_row(t, 'red', 'black', row_num)
##        row_num += 1
##    

def draw_square(t, width):
    for side in range(4):
        t.forward(width)
        t.right(90)

def draw_row(t, color1, color2):
    for square in range(4):
        t.fillcolor(color1)
        t.begin_fill()
        draw_square(t, 100)
        t.end_fill()
        t.forward(100)
        t.fillcolor(color2)
        t.begin_fill()
        draw_square(t, 100)
        t.end_fill()
        t.forward(100)

def checkerboard(tortoise):
    t = tortoise
    t.up()
    t.backward(400)
    t.right(90)
    t.backward(400)
    t.left(90)
    t.down()

    for row in range(4):
        # wrt range(4) -- it draws 4 pairs of rows, each of those two-row pairs alternating
        #   red-black and black-red. 
        draw_row(t, 'red', 'black')
        t.up()
        t.backward(800)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.down()

        draw_row(t, 'black', 'red')
        t.up()
        t.backward(800)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.down()

tortoise = setup()

##draw_row(tortoise, 'red', 'black')
##tortoise.setheading(90)
checkerboard(tortoise)
