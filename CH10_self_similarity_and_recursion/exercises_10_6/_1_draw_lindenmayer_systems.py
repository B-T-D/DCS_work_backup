import turtle

def draw_L_system(tortoise, string, angle, distance):
    """Draws the picture described by the given L-system string.

    Returns:
        None
    """
    for character in string:
        if character == 'F':
            tortoise.forward(distance)
        if character == '-':
            tortoise.left(angle)
        if character == '+':
            tortoise.right(angle)
    # solman is broken on this (again, similar in later 10.5 exercises)--
    #   refers to george instead of tortoise. 

def main():
    george = turtle.Turtle()
    screen = george.getscreen()
    george.hideturtle()

##    draw_L_system(george, 'F-F++F-F', angle=60, distance=10)
##
##    strings = ['F-F++F-F++F-F++F-F++F-F++F-F']
##    draw_L_system(george, strings[0], angle=60, distance=20)

    draw_L_system(george, 'FX-YF-FX+YF-FX-YF', angle=90, distance=20)

    screen.update()
    screen.exitonclick()

if __name__ == '__main__':
    main()
