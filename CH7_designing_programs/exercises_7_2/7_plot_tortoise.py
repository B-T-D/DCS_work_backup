import turtle

def plot(tortoise, n):
    """
    Precondition:
        tortoise is a turtle.Turtle() object
        n is a positive integer representing the extent of x values             

    Postcondition:
        Moves the turtle graphics drawing pen along the curve given by
        n ** 2, up to the value of n + 1
    """
    assert isinstance(tortoise, turtle.Turtle), \
           'tortoise must be a turtle.Turtle object'
    assert isinstance(n, int) and n > 0, \
           'n must be a positive integer'
    for x in range(-n, n + 1):
        tortoise.goto(x, x * x)


tortoise = turtle.Turtle()
##plot(tortoise, 5)
plot(tortoise, -5)
