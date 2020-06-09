from class_pair import Pair
from matplotlib import pyplot

def plot_flight_data(data):
    """
    Args:
        data (list): a list of pari objects representing times and altitudes
    """
    x_vals = []
    y_vals = []
    for pair in data:
        x_vals.append(pair.get_first())
        y_vals.append(pair.get_second())

    pyplot.plot(x_vals, y_vals)
    pyplot.xlabel("Time since takeoff")
    pyplot.ylabel("Altitude")
    pyplot.show()

# list[tuple(mins elapsed, altitude), ...]
data = [(0, 0),
        (5, 1000),
        (10, 5000),
        (15, 7500),
        (20, 8000),
        (25, 8000),
        (30, 12000),
        (35, 15000),
        (40, 25000),
        (45, 25000),
        (50, 25000)]
pairs = []
for d in data:
    pair = Pair(d[0], d[1])
    pairs.append(pair)

plot_flight_data(pairs)
