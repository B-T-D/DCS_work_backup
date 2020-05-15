import turtle
import random
##import lehmer_prng
    # Not getting this to work 2020-04-14 19:56, and it's not the thing
        # to focus on right now.

def test_random(n, random_func='random.random()'):
    """
    Args:
        n (int): Number of trials
        random_func (str): Random function to visually test. Should be a function
            that returns pseudorandom numbers in interval [0, 1).
    """
    tortoise = turtle.Turtle()
    screen = tortoise.getscreen()
    screen.setworldcoordinates(0, 0, 1, 1) # lower left is (0, 0), upper right (1, 1)
    screen.tracer(100) # Only draw every 100 updates
    tortoise.up()
    tortoise.speed(0)

    # draw the points here
    seed = 1
    r = seed
##    m = 5
    m = 2 ** 31 - 1
##    a = 13
    a = 16807
    
    for i in range(n):
##        x = eval(random_func)
##        y = eval(random_func)
        r = lehmer(r, m, a)
        x = r / m
        r = lehmer(r, m, a)
        y = r / m
        tortoise.goto(x, y)
        tortoise.dot()

    screen.update() # ensure that all updates are drawn
    screen.exitonclick()

def random_sequence(length, seed):
    """Returns a list of Park-Miller pseudorandom numbers.

    Args:
        length (int): Number of pseudorandom numbers to generate
        seed (int): The initial seed

    Returns:
        (list): List of Park-Miller pseudorandom numbers containing
        the specified number of elements, in the interval [0, 1).
    """

    r = seed
    m = 2 ** 31 - 1
    a = 16807
    rand_list = []
    for index in range(length):
        r = lehmer(r, m, a)
        rand_list.append(r / m)
    return rand_list

def lehmer(r, m, a):
    """Computes the next pseudorandom number using a Lehmer PRNG.

    Args:
        r (int): Seed or previous pseudorandom number
        m (int): A prime number
        a (int): An integer between 1 and m - 1

    Returns:
        (int): Next pseudorandom number in the sequence.
    """

    return (a * r) % m

def main():
    n = 100
##    func = 'random.random()'
##    func = 'random_sequence()'    
##    test_random(n, func)
    test_random(n)

main()
    
