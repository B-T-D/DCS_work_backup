from graph_from_txt import read_graph

def my_average_distance(network):
    """Returns the average distance between every pair of nodes in a
    network."""
    # abandoned
    
    distances = 0
    pairs = 0
    # return the distances for each node and average all of that nodes distances
    #   one by one, append to the distances list, then do the next node
    for node in network:
        distance = get_distances(network, node)
        for d in distance:
            distances += distance[d]
            pairs += 1
    # divide it by number of pairs not number of nodes
##    return distances / pairs
    # ^^ wrong. Need to divide it by the total number of possible neighbors,
    #   i.e. the same (k * (k - 1) / 2)

def average_distance(network):
    # solman
    total_distance = 0
    n = len(network) # number of nodes
    nodes = list(network.keys())
    for index1 in range(len(nodes) - 1):
        source = nodes[index1]
        dist, pred = bfs(network, source)
        for index2 in range(index1 + 1, len(nodes)):
            dest = nodes[index2]
            if dist[dest] == float('inf'):
                total_distance = total_distance + n # assigning the total distance
                    # to be the number of nodes in network
            else:
                total_distance = total_distance + dist[dest]
    return total_distance / (n* (n - 1) / 2)

def bfs(network, source):
    """Version without the internal 'visited' tracker dict."""
    distance = {}
    predecessor = {}
    for node in network:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[source] = 0
    queue = [source]
    while queue != []:
        front = queue.pop(0)
        for neighbor in network[front]:
            if distance[neighbor] == float('inf'):
                distance[neighbor] = distance[front] + 1
                predecessor[neighbor] = front
                queue.append(neighbor)
    return distance, predecessor

def get_distances(network, source):
    """Uses bfs to return all distances for a given source node."""
    distance = {}
    for node in network:
        distance[node] = len(network) # per the book's instructions
    distance[source] = 0 # this will end up overwriting the default value for all of them...
    queue = [source]
    while queue != []:
        front = queue.pop(0)
        for neighbor in network[front]:
            if distance[neighbor] == len(network):
                distance[neighbor] = distance[front] + 1
                queue.append(neighbor)
    return distance


network = read_graph('clusters.txt')
actual = average_distance(network)
print(actual)

network = read_graph('grid.txt')
actual = average_distance(network)
print(actual)

