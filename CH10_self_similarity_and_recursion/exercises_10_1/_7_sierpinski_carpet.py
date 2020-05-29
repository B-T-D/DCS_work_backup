import turtle

def carpet(tortoise, upper_left, width, depth):
    """Draws a Sierpinski carpet with the given depth.

    Args:
        upper_left (tuple): Upper left corner of the fractal
        width (int): Overall width of the fractal.
    """
    subwidth = width / 3
    if depth <= 0:
        draw_square(tortoise, upper_left, width, color='blue')
##        tortoise.up()
##        tortoise.goto(upper_left[0] + subwidth, upper_left[1] - 2* subwidth)
##        tortoise.fillcolor(colors)
##        tortoise.begin_fill()
##        tortoise.forward(subwidth)
##        tortoise.right(90)
##        tortoise.forward(subwidth)
##        tortoise.right(90)
##        tortoise.forward(subwidth)
##        tortoise.right(90)
##        tortoise.end_fill()
##        tortoise.setheading(90)
    else:
        subsquare_upper_lefts = [upper_left,
                                 (upper_left[0], upper_left[1] - subwidth),
                                 (upper_left[0], upper_left[1] - (2 * subwidth)),
                                 (upper_left[0] + subwidth, upper_left[1]),
                                 (upper_left[0] + subwidth, upper_left[1] - 2 * subwidth),
                                 (upper_left[0] + 2 * subwidth, upper_left[1]),
                                 (upper_left[0] + 2 * subwidth, upper_left[1] - subwidth),
                                 (upper_left[0] + 2 * subwidth, upper_left[1] - 2 * subwidth)
                                 ]
        for s in subsquare_upper_lefts:
            carpet(tortoise, s, subwidth, depth - 1)
        carpet(tortoise, upper_left, width, depth - 1)

def draw_square(tortoise, upper_left, width, color):
    subwidth = width / 3
    tortoise.up()
    tortoise.goto(upper_left[0] + subwidth, upper_left[1] - 2* subwidth)
    tortoise.fillcolor(color)
    tortoise.begin_fill()
    tortoise.forward(subwidth)
    tortoise.right(90)
    tortoise.forward(subwidth)
    tortoise.right(90)
    tortoise.forward(subwidth)
    tortoise.right(90)
    tortoise.end_fill()
    tortoise.setheading(90)
        
    

def draw_outer_square_reference(tortoise, upper_left, width):
    """Draws the outermost square for reference."""
    tortoise.up()
    tortoise.goto(upper_left)
    tortoise.down()
    tortoise.forward(width)
    tortoise.right(90)
    tortoise.forward(width)
    tortoise.right(90)
    tortoise.forward(width)
    tortoise.right(90)
    tortoise.forward(width)


def main():
    george = turtle.Turtle()
    width = 300
    upper_left = (-200, 200)
    george.speed(0)
    george.up()
    george.goto(upper_left)
    george.write('upper_left')
    draw_outer_square_reference(george, upper_left, width)
    carpet(george, upper_left, width, 2)
    

main()
