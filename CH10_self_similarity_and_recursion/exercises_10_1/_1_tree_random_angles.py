import turtle
import random

def tree(tortoise, length, depth):
    """Recursively draw a tree with turtle graphics.

    Args:
        tortoise (Turtle): a Turtle object
        length (int): the length of the trunk
        depth (int): the desired depth of recursion

    Returns:
        None
    """
    # base case, non-recursive:
    if depth <= 1:
        tortoise.forward(length) # up and back by length, then execution over
        tortoise.backward(length)
    # the recursive case:
    else:
        tortoise.forward(length)
        angle_1 = random.randrange(10, 60)
        angle_2 = random.randrange(10, 60)
        tortoise.left(angle_1) # half of the tortoise.right turn angle
        length_shrink_1 = random.uniform(0.5, 0.75)
        length_shrink_2 = random.uniform(0.5, 0.75)
        tree(tortoise, length * length_shrink_1, depth - 1) # eventually you end up calling it with depth <= 1
        tortoise.right(angle_1 + angle_2)                #...at which point the base case happens instead of the recursive case...
        tree(tortoise, length * length_shrink_2, depth - 1) # ...allowing execution to finish.
        tortoise.left(angle_2)
        tortoise.backward(length)

def main():
    george = turtle.Turtle()
    george.speed(0)
    george.left(90)
    tree(george, 100, 7)
    screen = george.getscreen()
    screen.exitonclick()

main()
