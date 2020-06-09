class Pair:
    """An ordered pair class."""

    def __init__(self, a = 0, b = 0):
        """Constructor initializes a Pair object to [0, 0].

        Args:
            self (pair): a Pair object.

        Returns:
            None
        """

        self._pair = [a, b]

    # Accessor methods:
    def get_first(self):
        """Return the first value of the pair object self."""
        return self._pair[0]
    
    def get_second(self):
        """Return the second value of the pair object self."""
        return self._pair[1]

    def get(self):
        """Return the [a, b] list representing self.

        Returns:
            (list): the [a, b] list representing self
        """
        return self._pair

    def add(self, pair2):
        """Return a new Pair representing the component-wise sum of self and
        pair2.

        Args:
            self (Pair object): a Pair object
            pair2 (Pair object): another Pair object

        Returns:
            (Pair object): new Pair object representing the component-wise
                sum.
        """
        sum_A = self._pair[0] + pair2._pair[0]
        sum_B = self._pair[1] + pair2._pair[1]
        return Pair(sum_A, sum_B)

    def subtract(self, pair2):
        """Return a new pair representing the component-wise difference of self
        and pair2."""
        diff_A = self._pair[0] - pair2._pair[0]
        diff_B = self._pair[1] - pair2._pair[1]
        return Pair(diff_A, diff_B)

    # Mutator methods:
    def set(self, a, b):
        """Set the two values in self.

        Args:
            a (int or float): a number representing a new first value for self
            b (int or float): a number representing a new second value for self

        Returns:
            None
        """

        self._pair[0] = a
        self._pair[1] = b

    def scale(self, scalar):
        """Multiply the values in self by a scalar value.

        Args:
            self: a Pair object
            scalar (int or float): a number by which to scale the values in self

        Returns:
            None
        """

        self.set(self._pair[0] * scalar, self._pair[1] * scalar)

    ###

    def round(self):
        """Rounds each value in the pair to the nearest integer."""
        self._pair[0] = round(self._pair[0])
        self._pair[1] = round(self._pair[1])
        

def centroid(points):
    """Compute the ventroid of a list of Pair objects.

    Args:
        points (list): a list of Pair objects

    Returns:
        (Pair): a Pair object representing the centroid of the points.
    """
    n = len(points)
    if n == 0:
        return None
    sum = Pair() # sum is the Pair(0, 0)
    for point in points:
        sum = sum.add(point)
    sum.scale(1 / n) # divide sum by the number of points
    return sum

def main():

    homes = [Pair(0.5, 5), Pair(3.5, 2), Pair(4, 3.5), Pair(5, 2), Pair(7, 1)]
    central = centroid(homes)
    print(central.get())

    mypair = Pair(3.14159, 3.333333)
    mypair.round()
    print(mypair.get())
    

if __name__ == '__main__':
    main()
