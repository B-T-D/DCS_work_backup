import random

def random_range(a, b):
    """Returns pseudorandom integer in [a..b],"""
    number = int(a + random.random() * ((b + 1) - a))
    return number

    # Book does (b - a + 1) but should be mathematically same thing. 

for i in range(25):
    print(random_range(1,4))
