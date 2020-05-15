#!/usr/bin/env python3

def readGraph(fileName):
    pass

def clusteringCoefficient(network, node):
    """Compute the local clustering coefficient for a node.
    
    Parameters:
        network: a graph represented by a dictionary
        node: a node in the network
        
    Return value: the local clustering coefficient of node
    """
    
    neighbors = network[node]
    numNeighbors = len(neighbors)
    if numNeighbors <= 1:
        return 0
    numLinks = 0
    for index1 in range(len(neighbors) - 1):
        for index2 in range(index1 + 1, len(neighbors)):
            neighbor1 = neighbors[index1]
            neighbor2 = neighbors[index2]
            if neighbor1 != neighbor2 and neighbor1 in network[neighbor2]:
                numLinks = numLinks + 1
    return numLinks / (numNeighbors * (numNeighbors - 1) / 2)
    
def main():
    graph = {'Amelia': ['Beth', 'Caroline', 'Lillian', 'Nick'],
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
              
    cc = clusteringCoefficient(graph, 'Beth')
    print(cc)
    
    graph = readGraph('facebook/facebook_small1.txt')
    cc = clusteringCoefficient(graph, '80')
    print(cc)
    
main()
