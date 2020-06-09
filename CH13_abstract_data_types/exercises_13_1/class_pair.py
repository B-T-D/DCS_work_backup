class Pair:
    """An ordered pair class."""

    def __init__(self, a = 0, b = 0):
        """Constructor initializes a Pair object to (0, 0).

        Args:
            self (pair): a Pair object.

        Returns:
            None
        """

        self._a = a # the pair's first value
        self._b = b # the pair's second value

    # Accessor methods:
    def get_first(self):
        """Return the first value of the pair object self."""
        return self._a
    
    def get_second(self):
        """Return the second value of the pair object self."""
        return self._b

    def get(self):
        """Return the (a, b) tuple representing self.

        Returns:
            (tuple): the (a, b) tuple representing self
        """
        return (self._a, self._b)

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
        sum_A = self._a + pair2._a
        sum_B = self._b + pair2._b
        return Pair(sum_A, sum_B)

    def subtract(self, pair2):
        """Return a new pair representing the component-wise difference of self
        and pair2."""

        diff_A = self._a - pair2._a
        diff_B = self._b - pair2._b
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

        self._a = a
        self._b = b

    def scale(self, scalar):
        """Multiply the values in self by a scalar value.

        Args:
            self: a Pair object
            scalar (int or float): a number by which to scale the values in self

        Returns:
            None
        """

        self.set(self._a * scalar, self._b * scalar)

    ###

    def round(self):
        """Rounds each value in the pair to the nearest integer."""
        self._a = round(self._a)
        self._b = round(self._b)
        

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
    
##    pair = Pair()
##    print(pair._a)
##    print(pair.get_second())
##
##    mypair = Pair(0, 18)
##    print(mypair.get_second())
##    print(mypair.get())
####    help(pair)
##
##    print('----')
##    duo1 = Pair(3, 8)
##    duo2 = Pair(4, 5)
##    sum = duo1.add(duo2) # sum is assigned Pair(7, 13)
##    print(sum.get()) # prints "(7, 13)"
##    diff = duo1.subtract(duo2)
##    print(diff.get())
##    duo1.set(5, 5)
##    print(duo1.get())
##    duo1.scale(20)
##    print(duo1.get())
if __name__ == '__main__':
    main()
