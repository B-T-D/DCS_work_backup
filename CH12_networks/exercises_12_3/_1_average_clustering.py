from graph_from_txt import read_graph

def clustering_coefficient(network, node): # book's from in-text
    """Compute the local clustering coefficient for a node.

    Args:
        network (dict): a graph represented by a dictionary
        node: a node in the network

    Returns:
        (float): the local clustering coefficient of node.
    """
    neighbors = network[node]
    num_neighbors = len(neighbors)
    if num_neighbors <= 1:
        return 0
    num_links = 0
    for index1 in range(len(neighbors) - 1):
        for index2 in range(index1 + 1, len(neighbors)):
            neighbor1 = neighbors[index1]
            neighbor2 = neighbors[index2]
            if neighbor1 != neighbor2 and neighbor1 in network[neighbor2]:
                num_links += 1
    return num_links / (num_neighbors * (num_neighbors - 1) / 2)

def average_clustering_coefficient(network):
    """Returns the average local clustering coefficient for a network."""
    coefficients = 0
    for key in network:
        coefficients += clustering_coefficient(network, key)
    return coefficients / len(network)

network = read_graph('grid.txt')
print(average_clustering_coefficient(network))

network = read_graph('clusters.txt')
print(average_clustering_coefficient(network))

