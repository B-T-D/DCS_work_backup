def friends_of_friends(network, node):
    """Find new neighbors-of-neighbors of a node in a network (return each
    neighbor's neighborhood).

    Args:
        network (dict): a graph represented by a python dict
        node: a node in the network

    Returns:
        (list): a list of new neighbors-of-neighbors of nodes
    """

    suggestions = []
    neighbors = network[node]
    for neighbor in neighbors: # neighbors of node
        for neighbor2 in network[neighbor]: # neighbors of each neighbor
            if neighbor2 != node and \
               neighbor2 not in neighbors and \
               neighbor2 not in suggestions:
                suggestions.append(neighbor2)
    return suggestions

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



suggestions = friends_of_friends(network, 'Cathy')
print(suggestions)
print(friends_of_friends(network, 'Lillian'))


# this doesn't quite work. You'd have to go back through original dict and
#   add the redundant listings. E.g. add Ted for Cathy.
for key, value in additions.items():
    network[key] = value
    for key2, val2 in network.items():
        if key2 in value: # if that node in the original net is among the added-person's friends list
            val2.append(key)


print(friends_of_friends(network, 'Dave'))
