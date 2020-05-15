import random
import matplotlib.pyplot as pyplot

def normal_hist(mean, std_dev, trials):
    """Produces histogram of trials values returned by the gauss function
    with the given mean and standard deviation."""

    sequence = []
    for i in range(trials):
        sequence.append(random.gauss(mean, std_dev))

    print(sequence)

    pyplot.hist(sequence, 100) # 100 buckets
    pyplot.show()

    


def main():
    mean = 0
    std_dev = 0.25
    trials = 100000
    normal_hist(mean, std_dev, trials)

main()
