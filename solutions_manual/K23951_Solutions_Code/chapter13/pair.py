#!/usr/bin/env python3

""" pair.py """

class Pair:
    """An ordered pair class."""
    
    def __init__(self, a = 0, b = 0):
        """Constructor initializes a Pair object to (a, b).
        
        Parameter:
            self: a Pair object
            
        Return value: None
        """
        
        self._a = a   # the pair's first value
        self._b = b   # the pair's second value

    def getFirst(self):
        """Return the first value of self.
        
        Parameter:
            self: a Pair object
            
        Return value: the first value of self
        """
        
        return self._a
        
    def getSecond(self):
        """Return the second value of self.
        
        Parameter:
            self: a Pair object
            
        Return value: the second value of self
        """
        
        return self._b

    def get(self):
        """Return the (a, b) tuple representing self.
        
        Parameter:
            self: a Pair object
            
        Return value: the (a, b) tuple representing self
        """
        
        return (self._a, self._b)
        
    def add(self, pair2):
        """Return a new Pair representing the component-wise sum 
           of self and pair2.
           
        Parameters:
            self: a Pair object
            pair2: another Pair object
            
        Return value: a Pair object representing self + pair2
        """
       
        sumA = self._a + pair2._a
        sumB = self._b + pair2._b
        return Pair(sumA, sumB)
        
    def subtract(self, pair2):
        """Return a new Pair representing the component-wise 
           difference between self and pair2.
           
        Parameters:
            self: a Pair object
            pair2: another Pair object
            
        Return value: a Pair object representing self - pair2
        """
       
        diffA = self._a - pair2._a
        diffB = self._b - pair2._b
        return Pair(diffA, diffB)
    
    def set(self, a, b):
        """Set the two values in self.
        
        Parameters:
            self: a Pair object
            a: a number representing a new first value for self
            b: a number representing a new second value for self
            
        Return value: None
        """
        
        self._a = a
        self._b = b
        
    def scale(self, scalar):
        """Multiply the values in self by a scalar value.
        
        Parameters:
            self: a Pair object
            scalar: a number by which to scale the values in self
                        
        Return value: None
        """
        
        self.set(self._a * scalar, self._b * scalar)
        
def centroid(points):
    """Compute the centroid of a list of Point objects.
    
    Parameter:
        points: a list of Point objects
        
    Return value: 
        a Point object representing the centroid of the points
    """
    
    n = len(points)
    if n == 0:
        return None
    sum = Pair()
    for point in points:
        sum = sum.add(point)
    sum.scale(1 / n)
    return sum
    
def main():
    homes = [Pair(0.5, 5), Pair(3.5, 2), Pair(4, 3.5), 
             Pair(5, 2), Pair(7, 1)]
    central = centroid(homes)
    print(central.get())
    
main()
