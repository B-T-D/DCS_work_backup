import turtle

def hilbert(tortoise, reverse, depth):
    """Draws a Hilbert space-filling curve with the given depth. (Bool) reverse
    indicates which mode the algorithm should draw in."""
    length = 30
    if reverse:
        turn = 270
        opposite = 90
    else:
        turn = 90
        opposite = 270
    if depth < 0:
        tortoise.hideturtle()
        tortoise.showturtle()# filler 
    else:
        tortoise.right(turn)
        hilbert(tortoise, not(reverse), depth - 1)
        tortoise.forward(length)
        tortoise.right(opposite)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.forward(length)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.right(opposite)
        tortoise.forward(length)
        hilbert(tortoise, not(reverse), depth - 1)
        tortoise.right(turn)

def sm_hilbert(tortoise, reverse, depth):
    # Easiest way to have it do nothing is just say if depth >= 0.
        # Don't need an if/else spelling out if depth < 0. I.e. spelling out
        # to do nothing. 
    if depth >= 0:
        if reverse:
            angle = -90
        else:
            angle = 90
        tortoise.right(angle)
        hilbert(tortoise, not reverse, depth - 1)
        tortoise.forward(10)
        tortoise.left(angle)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.forward(10)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.left(angle)
        tortoise.forward(10)
        hilbert(tortoise, not reverse, depth - 1)
        tortoise.right(angle)
    # something looks wrong with book's when it draws--some of the lines pass
    #   too close together. 

def main():
    george = turtle.Turtle()
    george.speed(0)
    sm_hilbert(george, False, 2)
##    hilbert(george, False, 2)
    george.pencolor('orange')
    george.write('orange for reverse=True call')
    sm_hilbert(george, True, 2)
##    hilbert(george, True, 2)

main()
