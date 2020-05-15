import math

def volume_sphere(radius):
    """
    Precondition:
        Radius is a positive float or integer.

    Postcondition:
        Returns the volume of a sphere with radius of radius, as a float object.
        
    """
    assert isinstance(radius, int) or isinstance(radius, float), \
           'Radius must be an integer or floating point number.'

    assert radius > 0, 'Radius must be greater than zero'

    return (4 / 3) * math.pi * (radius ** 3)

tests = [1, 2, 3, 4.7, 0, -1, 9.2, '9']

for t in tests:
    print(volume_sphere(t))
