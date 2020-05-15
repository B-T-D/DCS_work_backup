#!/usr/bin/env python3

import random

def randomGraph(n, p):
    '''Return a uniform random graph with n vertices.
    
    Parameters:
        n: the number of nodes
        p: the probability that two nodes are connected
        
    Return value: a random graph
    '''
    
    graph = { }
    for node in range(n):            # label nodes 0, 1, ..., n-1
        graph[node] = [ ]            # graph has n nodes, 0 links
    
    for node1 in range(n - 1):
        for node2 in range(node1 + 1, n):
            if random.random() < p:         
                graph[node1].append(node2)  # add edge between
                graph[node2].append(node1)  #   node1 and node2
    return graph

def main():
    randGraph = randomGraph(24, 38 / 276)
    
main()
