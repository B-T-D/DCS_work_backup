import matplotlib.pyplot as pyplot

def ant(n):
    """Simulates the "ant on a rubber rope" problem. The rope is initially
    1m long and the ant walks 10 cm each minute. The rope is lengthened by an
    additional 1M at the end of each minute, with the ant riding along.

    Args:
        n (int): Number of minutes the ant walks

    Return:
        (float): Fraction of the rope traveled by the ant in n minutes.
    """

    total = 0
    for number in range(1, n + 1):
        total = total + (1 / number)
    return total / 10 


def reach_end():
    """Returns the number of minutes after which the ant will first have
    walked the full length of the rope."""

    rope_walked = 0
    n = 0
    while rope_walked < 1:
        rope_walked = ant(n)
        n += 1
    return n

def plot_ln_approximation(n):
    total = 0
    x_list = [] # Values of n to use for plot's x axis
    y_list = [] # Values of 'total' to use for the plot's y axis
    for number in range(1, n + 1):
        total = total + (1 / number)
        x_list.append(number)
        y_list.append(total)
    

    # pyplot
    pyplot.plot(x_list, y_list)
    pyplot.xlabel('n')
    pyplot.ylabel('y (total distance walked in ant illustration)')
    pyplot.show()


    return total / 10

try_list = [1, 10000, 25000, 100000]
for n in try_list:
    print(f"{n} minutes:\n\t{ant(n)}")

##print(reach_end())
plot_ln_approximation(30)
