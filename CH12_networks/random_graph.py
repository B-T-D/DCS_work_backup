import random
from matplotlib import pyplot

def random_graph(n, p):
    """Return a uniform random graph with n vertices.

    Args:
        n (int): the number of nodes
        p (float): the probability that two nodes are connected

    Returns:
        (dict): a random graph
    """

    graph = {}
    for node in range(n): # label nodes 0, 1, ..., n-1
        graph[node] = [] # graph has n nodes, 0 links

    for node1 in range(n - 1):
        for node2 in range(node1 + 1, n):
            if random.random() < p:
                graph[node1].append(node2) # add edge between node 1 and node2
                graph[node2].append(node1)
    return graph

def degree_distribution(network):
    """Return the degree distribution as a dict."""
    degree_distribution = {}
    for node in network:
        degree = len(network[node])
        if degree in degree_distribution:
            degree_distribution[degree] += 1
        else:
            degree_distribution[degree] = 1
    n = len(network)
    for d in degree_distribution:
        degree_distribution[d] /= n
    return degree_distribution

def plot_degree_dist(network):
    """Uses pyplot to plot network's degree distribution."""
    deg_dist = degree_distribution(network)
    degree = list(deg_dist.keys())
    frequency = list(deg_dist.values())
    pyplot.scatter(degree, frequency)
##    pyplot.plot(degree, frequency)
    pyplot.xlabel('Degree')
    pyplot.ylabel('Fraction of nodes')
    pyplot.xlim(0, max(degree) + 10)
    pyplot.show()

##graph = random_graph(24, 38/276)
graph = random_graph(24, 0.5)
plot_degree_dist(graph)
