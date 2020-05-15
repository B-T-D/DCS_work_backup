import random
import matplotlib.pyplot as pyplot

def uniform_hist(a, b, trials):
    """Produces a histogram of trials values in the range [a, b] returned by the
    random.uniform() function."""

    samples = []
    for i in range(trials):
        samples.append(random.uniform(a, b))

    pyplot.hist(samples, 100)
    pyplot.show()
    
def main():
    a = 0
    b = 5
    trials = 100000
    uniform_hist(a, b, trials)

main()
