import matplotlib.pyplot as pyplot
import random

def sum_random(n):
    """Returns the sum of n pseudorandom numbers in [0, 1).

    Args:
        n (int): Number of pseudorandom numbers to generate.

    Returns:
        (float): Sum of n pseudorandom numbers in [0, 1)
    """

    sum = 0
    for index in range(n):
        sum = sum + random.random()
    return sum

def sum_random_hist(n, trials):
    """Displays a histogram of sums of n pseudorandom numbers.

    Args:
        n (int): Number of pseudorandom numbers in each sum.
        trials (int): Number of sumbs to generate

        Returns:
            None
    """

    samples = []
    for index in range(trials):
        samples.append(sum_random(n))
    pyplot.hist(samples, 100)
    pyplot.show()

for i in [1, 2, 3, 10]:
    n = i
    sum_random_hist(n, 100000)
