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

def bfs_old(network, source):
    """Perform a breadth-first search on network, starting from source.

    Args:
        network (dict): a graph represented by a dict
        source: the node in network from which to start the BFS

    Returns:
        distance (dict): a dictionary with distances from source to each node.
        predecessor (dict): a dictionary listing the node preceding each node
            on the shortest path from it to the source.
    """

    visited = {}
    distance = {}
    predecessor = {}
    for node in network:
        visited[node] = False
        distance[node] = float('inf') # No path will return infinite distance
        predecessor[node] = None
    visited[source] = True
    distance[source] = 0
    queue = [source]
    while queue != []:
        front = queue.pop(0) # dequeue front node
        for neighbor in network[front]:
            if not visited[neighbor]: # if it's not in the list of ones already visited
                visited[neighbor] = True
                distance[neighbor] = distance[front] + 1
                predecessor[neighbor] = front
                queue.append(neighbor) # enqueue visited node
    return distance, predecessor

def path(network, source, dest):
    """Find a shortest path in network from source to dest.

    Args:
        network (dict): a graph represented by a dictionary
        source: the source node in network
        dest: the destination node in network

    Returns:
        (list): a list of the nodes along the shortest path, in the order
            they'd be reached on the trip.
    """
    all_distances, all_predecessors = bfs(network, source)
    path = []
    current = dest
    while current != source:
        path.insert(0, current) # insert at start of list for correct ordering
        current = all_predecessors[current]
    path.insert(0, source)

    return path

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

for key, value in additions.items():
    network[key] = value
    for key2, val2 in network.items():
        if key2 in value: # if that node in the original net is among the added-person's friends list
            val2.append(key)

print(bfs(network, 'Christina'))
print(f"Beth: {bfs(network, 'Beth')}")

predecessors = bfs(network, 'Beth')[1]

print(f"-----\nPredecessors for Beth:")
print(predecessors)
for predecessor in predecessors:
    print(predecessor)

print(f"------\nPath Beth to Tyler:")
print(path(network, 'Beth', 'Tyler'))

print("----Tyler to Caroline----")
print(f"All distances from Tyler:")
all_distances = bfs(network, 'Tyler')[0]
print(all_distances)
print(f"distance to Caroline: {all_distances['Caroline']}")
path = path(network, 'Tyler', 'Caroline')
print(f"path from Tyler to Caroline:\n\t{path}")

