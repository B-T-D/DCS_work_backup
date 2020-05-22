import turtle
import math

def sierpinski(tortoise, p1, p2, p3, depth):
    """Draws a Sierpinski triangle with the given depth.

    Args:
        p1 (tuple): coordinates for the triangle's first corner
        p2 (tuple): ++
        p3 (tuple): ++

    Returns:
        None
    """
    if depth <= 0:
        draw_triangle(tortoise, p1, p2, p3)
    else:
        mid1t2 = midpoint(p1, p2)
        mid2t3 = midpoint(p2, p3)
        mid3t1 = midpoint(p3, p1)

        # call sierp at depth -1 on each of the 3 midpoints in the current parent
        sierpinski(tortoise, p1, mid1t2, mid3t1, depth - 1)
        sierpinski(tortoise, mid1t2, p2, mid2t3, depth - 1)
        sierpinski(tortoise, mid3t1, mid2t3, p3, depth - 1)

        # ** until this recurses all the way down to depth zero, it's not yet time to
        #    "just draw a triangle". Just draw a triangle only ever happens at depth 0
        
        

def draw_triangle(tortoise, p1, p2, p3):
    """Draw an equilateral triangle with vertices p1, p2, p3"""
    dist_a = euclidean_distance(p1, p2)
    dist_b = euclidean_distance(p2, p3)
    dist_c = euclidean_distance(p3, p1)
    assert -0.00001 < dist_a - dist_b < 0.00001, f"fail, dist_a - dist_b was {dist_a - dist_b}"
    assert -0.00001 < dist_b - dist_c < 0.00001
    assert -0.00001 < dist_a - dist_c < 0.00001

    # KISS: if you know the points are equilateral...just put the drawing pen .down()
    #   and use .goto().

    tortoise.up()
    tortoise.goto(p1)
    tortoise.down()
    tortoise.goto(p2)
    tortoise.goto(p3)
    tortoise.goto(p1)
    
    return
    
def euclidean_distance(p1, p2):
    """Returns 2D euclidean distance between points"""
    xx = (p1[0] - p2[0]) ** 2
    yy = (p1[1] - p2[1]) ** 2
    return math.sqrt(xx + yy)
    
def midpoint(p1, p2):
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    return x, y


def main():
    print(euclidean_distance((0, 0), (0, 4)))
    george = turtle.Turtle()
    george.speed(0)
    p1 = (-200, 0)
    p2 = (200,0)
    side_length = euclidean_distance(p1, p2)
    altitude = (math.sqrt(3) / 2) * side_length
    base_midpoint = midpoint(p1, p2)
    p3 = (base_midpoint[0], altitude)
    print(p1, p2, p3)
    sierpinski(george, p1, p2, p3, -2)

# sm = solman

def sm_draw_triangle(tortoise, p1, p2, p3):
    pass
    # same as mine

def sm_midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sm_sierpinski(tortoise, p1, p2, p3, depth):
    if depth <= 0:
        draw_triangle(tortoise, p1, p2, p3)
    else:
        sierpinski(tortoise, p1, sm_midpoint(p1, p2), sm_midpoint(p1, p3), depth - 1)
        sierpinski(tortoise, p2, sm_midpoint(p2, p3), sm_midpoint(p2, p1), depth - 1)
        sierpinski(tortoise, p3, sm_midpoint(p3, p1), sm_midpoint(p3, p2), depth - 1)

def sm_main():
    george = turtle.Turtle()
    p1 = (-200, 0)
    p2 = (200,0)
    side_length = euclidean_distance(p1, p2)
    altitude = (math.sqrt(3) / 2) * side_length
    base_midpoint = midpoint(p1, p2)
    p3 = (base_midpoint[0], altitude)
    print(p1, p2, p3)
    sierpinski(george, p1, p2, p3, 5)

##main()
sm_main()
