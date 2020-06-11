import pair
import random

class Pointset:
    """Class that contains a collection of points. Each point is a pair.Pair()
    object."""

    def __init__(self, points=[]):
        """
        Args:
            points (list): a list of Pair objects
        """
        self._points = points

    def insert(self, point):
        """
        Args:
            point (Pair): a pair object
        """
        self._points.append(point)

    def length(self):
        return len(self._points)

    def __len__(self):
        return len(self._points)

    def centroid(self):
        """Returns the centroid of this set of points, as a Pair object."""
        n = len(self)
        if n == 0:
            return None
        sum = pair.Pair() # initialize sum as the pair (0, 0)
        for point in self._points:
            sum += point
        sum.scale(1 / n) # divide the sum by the number of points
        return sum
        

    def __str__(self):
        return repr([(point[0], point[1]) for point in self._points])


points = [pair.Pair(random.randint(0, 100),
                    random.randint(0, 100)) for i in range(4)]
for point in points:
    print(point)

pset = Pointset(points)
print(pset)
print(f"calling len on pset: {len(pset)}")
print(pset.centroid())

points = [(0, 0), (2, 0), (0, 2), (2, 2)]
pairified = [pair.Pair(i[0], i[1]) for i in points]
pset = Pointset(pairified)
print(f"second test pointset is \n\t{pset}")
expected = pair.Pair(1, 1) # centroid should be the point right in the middle
actual = pset.centroid()
assert actual == expected, f"actual {actual}, expected {expected}"
