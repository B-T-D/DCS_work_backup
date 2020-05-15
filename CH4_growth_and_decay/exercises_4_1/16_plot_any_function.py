import turtle, math

def plot(tortoise, n, f):
    """
        Args:
            f (str): Name or an arbitrary function that takes a single numerical
                argument and returns a number.
            n (float): Number to pass as the numerical argument to function f.
    """
    tortoise.up()
    tortoise.goto(-n * 10, f(-n))
    tortoise.down()
    for x in range(-n, n + 1):
        tortoise.goto(10* x, f(x))

def square(x):
    return x * x

def cube(x):
    return x * x * x

def line(x):
    return 2 * x + 4

def main():
    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setworldcoordinates(-1000, -1000, 1000, 1000)
    plot(george, 20, square)
    george.pencolor('blue')
    plot(george, 20, cube)
    george.pencolor('orange')
    plot(george, 20, line)
    screen.exitonclick()

main()
