import turtle, math

def plot_sine(tortoise, n):
    """Uses Turtle graphics to plot sin(x) from x = 0 to x = n degrees.

    Args:
         
    
    """

    for x in range(0, n + 1):
        tortoise.goto(x, math.sin(math.radians(x)))

def main():
    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setworldcoordinates(0, -1, 1080, 1)
    plot_sine(george, 360)

main()
