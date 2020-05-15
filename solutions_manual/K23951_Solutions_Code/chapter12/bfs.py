#!/usr/bin/env python3

def bfs(network, source):
    """Perform a breadth-first search on network, starting from source.
    
    Parameters:
        network: a graph represented by a dictionary
        source: the node in network from which to start the BFS
        
    Return value: a dictionary with distances from source to all nodes
    """
    
    visited = { }
    distance = { }
    for node in network:
        visited[node] = False
        distance[node] = float('inf')
    visited[source] = True
    distance[source] = 0
    queue = [source]
    while queue != [ ]:
        front = queue.pop(0)             # dequeue front node
        for neighbor in network[front]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[front] + 1
                queue.append(neighbor)   # enqueue visited node
    return distance

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
              
    distancesFromBeth = bfs(graph, 'Beth')
    print(distancesFromBeth)
    
    distanceBeth2Tyler = distancesFromBeth['Tyler']
    print(distanceBeth2Tyler)
    
main()
