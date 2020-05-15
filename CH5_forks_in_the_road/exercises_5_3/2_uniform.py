import random

def uniform(a, b):
    """Returns a number in the interval [a, b) using only the random.random()
    function."""

##    number = random.random()
##    number = number - a
##    number = number + b

# [Fail / abandon and codealong]

    # Book's:
    return a + random.random() * (b - a)
    
    return number

for i in range(50):
    print(uniform(1, 5))
