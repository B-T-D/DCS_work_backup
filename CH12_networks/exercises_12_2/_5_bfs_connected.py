def bfs(network, source):
    """Returns boolean indicating whether the graph is connected (True if
    there's a path between any pair of nodes."""
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
    # If no nodes still have infinity as their distance, the graph is a connected
    #   graph.
    for key in network:
        if distance[key] == float('inf'):
            return False
    return True
    
    return distance, predecessor

network = {'Amelia': ['Beth', 'Caroline', 'Lillian', 'Nick'],
            'Beth': ['Amelia', 'Cathy', 'Dave', 'Nick'],
            'Caroline': ['Amelia', 'Lillian', 'Nick'],
            'Cathy': ['Beth', 'Dave', 'Ted'],
            'Dave': ['Beth', 'Cathy', 'Christina'],
            'Lillian': ['Amelia', 'Caroline', 'Nick'],
            'Nick': ['Amelia', 'Beth', 'Caroline', 'Lillian'],
            'Ted': ['Cathy', 'Christina'],
            'Kevin': ['Christina'],
            'Vanessa': ['Christina'],
            'Christina': ['Kevin', 'Ted', 'Vanessa', 'Tyler', 'Ryder', 'Dave'],
            'Tyler': ['Christina', 'Ryder'],
            'Ryder': ['Tyler', 'Christina']}

expected = True
actual = bfs(network, 'Amelia')
assert actual == expected, f"actual {actual}, expected {expected}"

non_connected = {'A': ['B', 'C', 'D'],
                'B': ['A',],
                'C': ['A', 'D'],
                'D': ['A', 'C'],
                'E': []}

expected = False
actual = bfs(non_connected, 'A')
assert actual == expected, f"actual {actual}, expected {expected}"

print(bfs(non_connected, 'E'))
print(bfs(non_connected, 'C'))

