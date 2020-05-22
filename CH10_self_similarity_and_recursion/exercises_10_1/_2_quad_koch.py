import turtle

def quad_koch(tortoise, length, depth):
    """Draws the quadratic Koch curve with given segment length and depth.
    I.e. middle segment replaced with three sides of a square rather  than two
    sides of an equilateral triangle.
    """
    if depth == 0:
        tortoise.forward(length)
    else:
        quad_koch(tortoise, length / 3, depth - 1)
        tortoise.left(90)
        quad_koch(tortoise, length / 3, depth - 1)
        tortoise.right(90)
        quad_koch(tortoise, length / 3, depth - 1)
        tortoise.right(90)
        quad_koch(tortoise, length / 3, depth - 1)
        tortoise.left(90)
        quad_koch(tortoise, length / 3, depth -1)

def main():
    george = turtle.Turtle()
    quad_koch(george, 400, 3)


main()
