#!/usr/bin/env python3

def bfs(network, source):
    """ (docstring omitted) """
    
    visited = { }
    distance = { }
    predecessor = { }
    for node in network:
        visited[node] = False
        distance[node] = float('inf')
        predecessor[node] = None
    visited[source] = True
    distance[source] = 0
    queue = [source]
    while queue != [ ]:
        front = queue.pop(0)             # dequeue front node
        for neighbor in network[front]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[front] + 1
                predecessor[neighbor] = front
                queue.append(neighbor)   # enqueue visited node
    return distance, predecessor
    
def path(network, source, dest):
    """Find a shortest path in network from source to dest.
    
    Parameters:
        network: a graph represented by a dictionary
        source: the source node in network
        dest: the destination node in network
        
    Return value: a list containing a path from source to dest
    """
    
    allDistances, allPredecessors = bfs(network, source)
    
    path = [ ]
    current = dest
    while current != source:
        path.insert(0, current)
        current = allPredecessors[current]
    path.insert(0, source)
    
    return path

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
              
    pathBeth2Tyler = path(graph, 'Beth', 'Tyler')
    print(pathBeth2Tyler)
    
main()
