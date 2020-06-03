import random

def dfs(network, source, visited):
    """Performs a depth-first search on the given network, starting from the
    given source node.

    Args:
        visited (list): a blank list. Pass it in blank and the function fills
            it with all visited nodes.
    """
    for neighbor in network[source]:
        if neighbor not in visited:
            visited.append(neighbor)
            dfs(network, neighbor, visited)
    return visited

def solman_dfs(network, source, visited):
    if source in visited:
        return

    visited.append(source)

    for neighbor in network[source]:
        solman_dfs(network, neighbor, visited)

def connected(network):
    """Uses the dfs function to check if the network is a connected graph."""
    source = random.choice(list(network.keys())) # source node can be any in the nw
    visited = dfs(network, source, [])
    return len(visited) == len(network)

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

non_connected = {'Amelia': ['Beth', 'Caroline', 'Lillian', 'Nick'],
            'Beth': ['Amelia', 'Cathy', 'Dave', 'Nick'],
            'Caroline': ['Amelia', 'Lillian', 'Nick'],
            'Cathy': ['Beth', 'Dave', 'Ted'],
            'Dave': ['Beth', 'Cathy', 'Christina'],
            'Lillian': ['Amelia', 'Caroline', 'Nick'],
            'Nick': ['Amelia', 'Beth', 'Caroline', 'Lillian'],
            'Ted': ['Cathy', 'Christina'],
            'Kevin': ['Christina'],
            'Vanessa': [],
            'Christina': ['Kevin', 'Ted', 'Tyler', 'Ryder', 'Dave'],
            'Tyler': ['Christina', 'Ryder'],
            'Ryder': ['Tyler', 'Christina']}

visited = []
dfs(network, 'Beth', visited)

expected = True
actual = connected(network)
assert actual == expected, f"actual {actual}, expected {expected}"

expected = False
actual = connected(non_connected)
assert actual == expected, f"actual {actual}, expected {expected}"
