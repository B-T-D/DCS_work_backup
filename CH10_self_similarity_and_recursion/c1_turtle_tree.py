import turtle

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
        tortoise.left(30) # half of the tortoise.right turn angle
##        print(f"calling tree() recursively with length = {length * (2 / 3)} \
##and depth = {depth - 1}")
        tree(tortoise, length * (2 / 3), depth - 1) # eventually you end up calling it with depth <= 1
        tortoise.right(60)                #...at which point the base case happens instead of the recursive case...
        tree(tortoise, length * (2 / 3), depth - 1) # ...allowing execution to finish.
        tortoise.left(30)
        tortoise.backward(length)

def main():
    george = turtle.Turtle()
    george.speed(0)
    george.left(90)
    tree(george, 100, 12)
    screen = george.getscreen()
    screen.exitonclick()

main()
        
