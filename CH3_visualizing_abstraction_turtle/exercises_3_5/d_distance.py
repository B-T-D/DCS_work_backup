import math


def distance(x1, y1, x2, y2):
    """
    Computes the distance between two cartesian coordinate points.

    Args:
        x1 (float): the x coordinate of the first point.
        y1 (float): the y coordinate of the first point.
        x2 (float): x coordinate of second point.
        y2 (float): y coordinate of second point.

    Returns:
        (float): The straight-line distance between the two points.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print(distance(0, 0, 3, 4,))
