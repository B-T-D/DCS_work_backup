import turtle

def derive(string, productions, depth):
    """Recursively apply productions to axiom 'depth' times.

    Args:
        string (str): a string of L-system symbols (the axiom)
        productions (dict): a dictionary containing L-system productions
        depth (int): the number of times the productions are applied

    Returns:
        (str): the new string reflecting the application of productions.
    """

    if depth <= 0: # base case
        return string

    new_string = '' # beginning of recursive case
    for symbol in string:
        if symbol in productions:
            new_string = new_string + productions[symbol]
        else:
            new_string = new_string + symbol
    return derive(new_string, productions, depth - 1)

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

def L_system(axiom, productions, depth, angle, distance, position, heading):
    """
    Calls the derive function with the first three parameters, and then calls
    the draw_L_system function from Exercise 10.6.1 with the new string and the
    values of angle and distance. Last two parameters specify initial position
    and heading of the turtle object, before draw_L_system is called.

    Returns:
        None
    """
    george = turtle.Turtle()
    george.up()
    george.goto(position)
    george.setheading(heading)
    george.down()
    george.speed(0)
    george.hideturtle()
    screen = george.getscreen()
    
    string = derive(axiom, productions, depth)
    draw_L_system(george, string, angle, distance)
    
    
    pass

def test_main_for_derive():
    koch_productions = {'F': 'F-F++F-F'}
    result = derive('F', koch_productions, 3)
    print(result)

##axiom = 'F'
##productions = {'F': 'F-F++F-F'}
##depth = 5
##L_system(axiom, productions, depth, angle=60, distance=5, position=(-600, -200), heading=0)

##axiom = 'FX'
##productions = {'X': 'X-YF', 'Y': 'FX + Y'}
##angle = 90
##distance = 5
##position = (0, 0)
##heading = 0
##depth = 12
##L_system(axiom, productions, depth, angle, distance, position, heading)

# Axiom for koch snowflake:
axiom = 'F++F++F' # final correct one to draw a closed snowflake
productions = {'F': 'F-F++F-F'}
angle = 60
distance = 5
position = (-400, 0)
heading = 0
depth = 4
L_system(axiom, productions, depth, angle, distance, position, heading)


