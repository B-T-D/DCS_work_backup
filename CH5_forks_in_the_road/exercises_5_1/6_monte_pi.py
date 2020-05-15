import math, random


def monte_pi(darts):
    """
    Args:
        darts (int): Number of darts to throw in making the approximation.

    """

    # Set up the circle and the square without using classes
##    radius = 1
##    side_length = 2 * radius
##    square_area = side_length * side_length
##    circle_area = 3.14159 * radius ** 2

    # Simulate throwing darts

    # [Switching to book's for expediency]
    circle = 0
    for trials in range(darts):
        x = random.random() # Get a random x coordinate [b/c this returns in [0, 1) ]
        y = random.random()
        distance = math.sqrt(x**2 + y**2) # compute distance of that random x, y pair from the origin (0, 0)
        if distance <= 1: # If (x, y) is in the circle then count it
            circle = circle + 1
    pi = (circle / darts) * 4 # area = pi * (1)^2
    return pi

trials_counts = []
for i in range(8):
    trials_counts.append(10 ** i)

for i in trials_counts:
    print(f"{i} | {monte_pi(i)}")
    
