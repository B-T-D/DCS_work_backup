#!/usr/bin/env python3.3

import matplotlib.pyplot as pyplot
    
def writeGraph(graph, fileName):
    graphFile = open(fileName, 'w', encoding = 'utf-8')
    for node in graph:
        for node2 in graph[node]:
            if int(node) < int(node2):
                graphFile.write(node + ' ' + node2 + '\n')
    graphFile.close()
    
def readGraphChecks(fileName):
    """list of edges, only one direction included"""
    
    graphFile = open(fileName, 'r', encoding = 'utf-8')
    graph = { }
    for line in graphFile:
        edge = line.split()
        if edge[0] in graph and edge[1] in graph[edge[0]]:
            print('repeat forward:', edge)
        if edge[1] in graph and edge[0] in graph[edge[1]]:
            print('repeat backward:', edge)
        if edge[0] == edge[1]:
            print('loop:', edge)
            continue
        if edge[0] in graph:
            if edge[1] not in graph[edge[0]]:
                graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            if edge[0] not in graph[edge[1]]:
                graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    graphFile.close()
    return graph
    
def readGraph(fileName):
    """list of edges, only one direction included"""
    
    graphFile = open(fileName, 'r', encoding = 'utf-8')
    graph = { }
    for line in graphFile:
        edge = line.split()
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    graphFile.close()
    return graph
    
def readGraphChecksDirected(fileName):
    """list of edges, only one direction included"""
    
    graphFile = open(fileName, 'r', encoding = 'utf-8')
    graph = { }
    for line in graphFile:
        edge = line.split()
        if edge[0] in graph and edge[1] in graph[edge[0]]:
            print('repeat:', edge)
        if edge[0] == edge[1]:
            print('loop:', edge)
            continue
        if edge[0] in graph:
            if edge[1] not in graph[edge[0]]:
                graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
    graphFile.close()
    return graph
    
def readGraphDirected(fileName, swap = False):
    graphFile = open(fileName, 'r', encoding = 'utf-8')
    graph = { }
    for line in graphFile:
        edge = line.split()
        if swap:
            edge = [edge[1], edge[0]]
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
    graphFile.close()
    return graph
    
def writeGraphDirected(graph, fileName):
    graphFile = open(fileName, 'w', encoding = 'utf-8')
    for node in graph:
        for node2 in graph[node]:
            graphFile.write(node + ' ' + node2 + '\n')
    graphFile.close()

def readGraphNeighbors(fileName):
    """node neighbors"""
    
    graphFile = open(fileName, 'r', encoding = 'utf-8')
    graph = { }
    for line in graphFile:
        nodes = line.split()
        graph[nodes[0]] = nodes[1:]
    graphFile.close()
    return graph

def degreeDistribution(graph):
    counts = {}      
    for node in graph:
        degree = len(graph[node])
        if degree in counts:
            counts[degree] = counts[degree] + 1
        else:
            counts[degree] = 1         

    n = len(graph)
    for degree in counts:
        counts[degree] = counts[degree] / n
        
    degrees = list(counts.keys())
    fractions = list(counts.values())
    pyplot.plot(degrees, fractions, linewidth = 2)
    pyplot.xlabel('Degree')
    pyplot.ylabel('Fraction of nodes')
    pyplot.xlim(0, max(degrees) + 10)
    pyplot.show()
    
#     degrees.sort()
#     bigDegree = degrees[-10]
#     for node in graph:
#         degree = len(graph[node])
#         if degree >= bigDegree:
#             print(node, 'has degree', degree)
#             
#     count = 0
#     for node in graph:
#         degree = len(graph[node])
#         if degree > 15:
#             count = count + 1
#     print(count)
#     print(count / n)

def m(graph):
    sum = 0
    for node in graph:
        sum = sum + len(graph[node])
    return sum / 2

def fix_facebook():
    filename = '698.edges'
    graph = readGraph2(filename)
    print('n =', len(graph))
    print('m =', m(graph))
#    degreeDistribution(graph)

    writeGraph(graph, filename + '.1')
    
    print('Testing new file')
    graph = readGraph3(filename + '.1')
    print('n =', len(graph))
    print('m =', m(graph))
#    degreeDistribution(graph)


def fix_twitter():
    """Original file has repeated edges and loops."""
    
#     filename = '../twitter/twitter_combined.txt'
#     graph = readGraph3(filename)
#     print('n =', len(graph))
#     print('m =', m(graph))
#     degreeDistribution(graph)
# 
#     writeGraph(graph, filename + '.1')

#    print('Testing new file')
#    graph = readGraphDirected(filename + '.1')
    filename = '../twitter/twitter_fixed.txt'
    graph = readGraph(filename)
    print('n =', len(graph))
    print('m =', m(graph))
    degreeDistribution(graph)


def fix_web():
    """Original file has comments at top and is tab-delimited."""
    
#     filename = '../web/web-Google.txt'
#     graph = readGraphChecksDirected(filename)
#     print('n =', len(graph))
#     print('m =', m(graph))
#     degreeDistribution(graph)
# 
#     writeGraphDirected(graph, filename + '.1')
# 
#     print('Testing new file')
#     graph = readGraphDirected(filename + '.1')
    filename = '../web/web_fixed.txt'
    graph = readGraphDirected(filename)
    print('n =', len(graph))
    print('m =', m(graph) * 2)
    degreeDistribution(graph)

def fix_neighbors():    
    filename = '../clusters.txt'
    graph = readGraphNeighbors(filename)
    print('n =', len(graph))
    print('m =', m(graph))
    degreeDistribution(graph)

    writeGraph(graph, filename + '.1')

    print('Testing new file')
    graph = readGraph(filename + '.1')
    print('n =', len(graph))
    print('m =', m(graph))
    degreeDistribution(graph)

'''
0 (small1)
n = 333
m = 2519

348 (small2)
n = 224
m = 3192

414 (small3)
n = 150
m = 1693

686 (small4)
n = 168
m = 1656

107 (medium1)
n = 1034
m = 26749

698
n = 61
m = 270

1684 (medium2)
n = 786
m = 14024

1912 (medium3)
n = 747
m = 30025

3437 (small5)
n = 534
m = 4813

3980
n = 52
m = 146

twitter
n = 81306
m = 1342296

web
# Directed graph (each unordered pair of nodes is saved once): web-Google.txt 
# Webgraph from the Google programming contest, 2002
# Nodes: 875713 Edges: 5105039
# FromNodeId	ToNodeId

'''