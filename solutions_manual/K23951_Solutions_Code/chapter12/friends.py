#!/usr/bin/env python3

def friendsOfFriends(network, node):
    """Find new neighbors-of-neighbors of a node in a network.
    
    Parameters:
        network: a graph represented by a dictionary
        node: a node in the network
        
    Return value: a list of new neighbors-of-neighbors of node
    """
    
    suggestions = [ ]
    neighbors = network[node]
    for neighbor in neighbors:                # neighbors of node
        for neighbor2 in network[neighbor]:   # neighbors of neighbors
            if neighbor2 != node and \
               neighbor2 not in neighbors and \
               neighbor2 not in suggestions:
                suggestions.append(neighbor2)
    return suggestions

def main():
    graph = {'Amelia': ['Beth', 'Caroline', 'Lillian', 'Nick'],
             'Beth': ['Amelia', 'Cathy', 'Dave', 'Nick'],
             'Caroline': ['Amelia', 'Lillian', 'Nick'],
             'Cathy': ['Beth', 'Dave'],
             'Dave': ['Beth', 'Cathy'],
             'Lillian': ['Amelia', 'Caroline', 'Nick'], 
             'Nick': ['Amelia', 'Beth', 'Caroline', 'Lillian']}
             
    graph2 = {'Amelia': ['Beth', 'Caroline', 'Lillian', 'Nick'],
              'Beth': ['Amelia', 'Cathy', 'Dave', 'Nick'],
              'Caroline': ['Amelia', 'Lillian', 'Nick'],
              'Cathy': ['Beth', 'Dave', 'Ted'],
              'Dave': ['Beth', 'Cathy', 'Christina'],
              'Lillian': ['Amelia', 'Caroline', 'Nick'], 
              'Nick': ['Amelia', 'Beth', 'Caroline', 'Lillian'],
              'Ted': ['Cathy', 'Christina'],
              'Christina': ['Dave', 'Kevin', 'Ryder', 'Ted', 'Tyler', 'Vanessa'],
              'Kevin': ['Christina'],
              'Tyler': ['Christina', 'Ryder'],
              'Ryder': ['Christina', 'Tyler'],
              'Vanessa': ['Christina']}
              
    newFriends = friendsOfFriends(graph2, 'Dave')
    print(newFriends)
    
main()
