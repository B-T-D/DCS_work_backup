def max_degree(network):
    """Returns the maximum degree in a network represented by an adjacency
    list.

    Args:
        network (dict): adjacency list implemented as a python dict
    """
    max = 0
    for key in network.keys():
        degree = len(network[key])
        if degree > max:
            max = degree
    return max

def mean_degree(network):
    """Returns the mean degrees of the nodes in a network."""
    degrees = 0
    for key in network.keys():
        degrees += len(network[key])
    return degrees / len(network)
        

network = {'A': ['B', 'C', 'D'],
            'B': ['A', 'E'],
            'C': ['A', 'D', 'E'],
            'D': ['A', 'C'],
            'E': ['B', 'C']}

expected = 3

actual = max_degree(network)

assert actual == expected, f"actual {actual}, expected {expected}"

expected = 12 / 5
actual = mean_degree(network)
assert actual == expected, f"actual {actual}, expected {expected}"
