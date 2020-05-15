import random
import matplotlib.pyplot as pyplot


def sum_gauss_squared(k):

    sum = 0
    for j in range(k):
        sum = sum + random.gauss(0, 1) ** 2
    return sum

def plot_chi_squared(k, trials):
    """Produces a histogram of trials values, each of which is the sum of k
    squares of values given by the random.gauss() function with mean 0 and
    std 1. """

##    samples = []
##    for i in range(k):
##        value = random.gauss(0, 1)
##        value = value ** 2
##        samples.append(value)

    # Book's:
    samples = []
    for i in range(trials):
        sum = sum_gauss_squared(k)
        samples.append(sum)

    pyplot.hist(samples, 200)
    pyplot.show()

def main():
    k = 1
    trials = 10000
    plot_chi_squared(k, trials)

main()
    
    


