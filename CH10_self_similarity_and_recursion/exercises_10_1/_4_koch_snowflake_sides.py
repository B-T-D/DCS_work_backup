import turtle 

def koch(tortoise, length, depth):
    """Recursively draw a Koch curve.

    Args:
        tortoise (Turtle): a Turtle object
        length (int): the length of a line segment
        depth (int): the desired depth of recursion

    Returns:
        None
    """

    if depth == 0: # base case
        tortoise.forward(length)
    else:
        koch(tortoise, length / 3, depth - 1)
        tortoise.left(60)
        koch(tortoise, length / 3, depth - 1)
        tortoise.right(120)
        koch(tortoise, length / 3, depth - 1)
        tortoise.left(60)
        koch(tortoise, length / 3, depth -1)

def koch_snowflake(tortoise, length, depth, sides=3):
    """Recursively draw a Koch snowflake.

    Args:
        tortoise (Turtle): a Turtle object
        length (int): the length of a line segment
        depth (int): the desired depth of recursion
        sides (int): number of sides for the snowflake

    Returns:
        None
    """
    colors = ['red', 'green', 'blue', 'orange']
    for side in range(sides):
        koch(tortoise, length, depth)
        tortoise.right(360 / sides)
        try:
            tortoise.pencolor(colors[side])
        except IndexError:
            pass

def main():
    george = turtle.Turtle()
##    koch(george, 400, 3)
    george.speed(0)
    koch_snowflake(george, 200, 3, sides=5)
    screen = george.getscreen()
    screen.exitonclick()

if __name__ == '__main__':
    main()
