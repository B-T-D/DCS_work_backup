def bfs(network, source):
    """Perform a breadth-first search on network, starting from source.

    Args:
        network (dict): a graph represented by a dict
        source: the node in network from which to start the BFS

    Returns:
        distance (dict): a dictionary with distances from source to each node.
        predecessor (dict): a dictionary listing the node preceding each node
            on the shortest path from it to the source.
    """
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

def distance(network, source, dest):
    """Uses the bfs function to return the distance between two particular
    nodes."""
    all_distances = bfs(network, source)[0]
    return all_distances[dest]


network = {'Amelia': ['Beth', 'Caroline', 'Lillian', 'Nick'],
           'Beth': ['Amelia', 'Cathy', 'Dave', 'Nick'],
           'Caroline': ['Amelia', 'Lillian', 'Nick'],
           'Cathy': ['Beth', 'Dave'],
           'Dave': ['Beth', 'Cathy'],
           'Lillian': ['Amelia', 'Caroline', 'Nick'],
           'Nick': ['Amelia', 'Beth', 'Caroline', 'Lillian']}

additions = {'Ted': ['Cathy', 'Christina'],
             'Kevin': ['Christina'],
             'Vanessa': ['Christina'],
             'Christina': ['Kevin', 'Ted', 'Vanessa', 'Tyler', 'Ryder', 'Dave'],
             'Tyler': ['Christina', 'Ryder'],
             'Ryder': ['Tyler', 'Christina']}

# this doesn't quite work. You'd have to go back through original dict and
#   add the redundant listings. E.g. add Ted for Cathy.
for key, value in additions.items():
    network[key] = value
    for key2, val2 in network.items():
        if key2 in value: # if that node in the original net is among the added-person's friends list
            val2.append(key)

source = 'Beth'
dest = 'Tyler'
expected = 3
actual = distance(network, 'Beth', 'Tyler')
assert actual == expected, f"actual {actual}, expected {expected}"
