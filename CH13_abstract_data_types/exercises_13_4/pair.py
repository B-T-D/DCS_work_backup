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

    def __str__(self):
        """Return an '(a, b)' string representation of self."""

        return '(' + str(self._a) + ', ' + str(self._b) + ')'

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

    def __add__(self, pair2):
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

    def __sub__(self, pair2):
        """Return a new pair representing the component-wise difference of self
        and pair2."""

        diff_A = self._a - pair2._a
        diff_B = self._b - pair2._b
        return Pair(diff_A, diff_B)

    def __mul__(self, scalar):
        """Return a new Pair representing self multiplied by scalar."""

        return Pair(self._a * scalar, self._b * scalar)

    def __truediv__(self, scalar):
        return Pair(self._a / scalar, self._b / scalar)

    def __floordiv__(self, scalar):
        return Pair(self._a // scalar, self._b // scalar)

    def __eq__(self, pair2):
        """Return True if self and pair2 contain the same ordered pair, else
        False."""

        return (self._a == pair2._a) and (self._b == pair2._b)

    def __ne__(self, pair2):
        return (self._a != pair2._a) or (self._b != pair2._b)

    def __lt__(self, pair2):
        """Return whether self < pair2."""
        return (self._a < pair2._a) or \
               ((self._a == pair2._a) and (self._b < pair2._b))

    def __getitem__(self, index):
        """Return the first or second index value in self. For values other than
        0 or 1, return None."""
        if index == 0:
            return self._a
        if index == 1:
            return self._b
        return None

    def __setitem__(self, index, value):
        """Set the first or second index value in self to the given value."""
        if index == 0:
            self._a = value
        elif index == 1:
            self._b = value

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
        sum += point
    sum.scale(1 / n) # divide sum by the number of points
    return sum

def main():

    homes = [Pair(0.5, 5), Pair(3.5, 2), Pair(4, 3.5), Pair(5, 2), Pair(7, 1)]
    central = centroid(homes)
    print(central.get())

    mypair = Pair(3.14159, 3.333333)
    mypair.round()
    print(mypair)

    print(f"mypair is {mypair}")
    scalar = 4
    print(f"mypair * {scalar}: {mypair * scalar}")
    print(f"mypair / {scalar}: {mypair / scalar}")
    print(f"mypair // {scalar}: {mypair // scalar}")
    print(f"mypair == Pair(3, 3): {mypair == Pair(3, 3)}")
    print(f"mypair != Pair(4, 3): {mypair != Pair(4, 3)}")
    print(f"mypair < Pair(2, 4): {mypair < Pair(2, 4)}")
    print(f"mypair > Pair(2, 4): {mypair > Pair(2, 4)}")
    print(f"mypair[0]: {mypair[0]}")
    mypair[0] = 5000
    print(f"mypair[0] = 5000: {mypair[0]}")
    
    
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
