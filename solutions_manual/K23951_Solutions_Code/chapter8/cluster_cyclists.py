#!/usr/bin/env python3

import random
import math
import matplotlib.pyplot as pyplot

def distance(p, q):
    pass
    
def centroid(cluster, data):
    pass

def kmeans(data, k, iterations):
    """Cluster data into k clusters using the given number of
       iterations of the k-means clustering algorithm.
    
    Parameters:
        data: a list of points
        k: the number of desired clusters
        iterations: the number of iterations of the algorithm
        
    Return value:
        a tuple containing the list of clusters and the list
        of centroids; each cluster is represented by a list 
        of indices of the points assigned to that cluster
    """
    
    n = len(data)
    centroids = random.sample(data, k)
    
    for step in range(iterations):
        clusters = []
        for i in range(k):
            clusters.append([])
        
        for dataIndex in range(n):
            minIndex = 0
            for clusterIndex in range(1, k):
                dist = distance(centroids[clusterIndex], data[dataIndex])
                if dist < distance(centroids[minIndex], data[dataIndex]):
                    minIndex = clusterIndex
            clusters[minIndex].append(dataIndex)
        
        for clusterIndex in range(k):
            centroids[clusterIndex] = centroid(clusters[clusterIndex], data)

    return (clusters, centroids)
    
def readFile(filename):
    """
    Read locations of 2012 bicycle accidents in Manhattan 
    into a list of tuples.
    
    Parameter:
        filename: the name of the data file
        
    Return value: a list of (longitude, latitude) tuples
    """
    
    inputFile = open(filename, 'r', encoding = 'utf-8')
    header = inputFile.readline()
    data = [ ]
    for line in inputFile:
        row = line.split('\t')
        borough = int(row[0])
        year = int(row[2])
        if (borough == 1) and (year == 2012):
            longitude = float(row[4])
            latitude = float(row[5])
            data.append( (longitude, latitude) )
    inputFile.close()
    return data

def plotClusters(clusters, data, centroids):
    """
    Plot clusters and centroids in unique colors.
    
    Parameters:
        clusters: a list of k lists of data indices
        data: a list of points
        centroids: a list of k centroid points
        
    Return value: None
    """
    
    colors = ['blue', 'red', 'yellow', 'green', 'purple', 'orange']
    for clusterIndex in range(len(clusters)):   # plot clusters of points
        x = []
        y = []
        for dataIndex in clusters[clusterIndex]:
            x.append(data[dataIndex][0])
            y.append(data[dataIndex][1])
        pyplot.scatter(x, y, 10, color = colors[clusterIndex])
        
    x = []
    y = []
    for centroid in centroids:    # plot centroids
        x.append(centroid[0])
        y.append(centroid[1])
    pyplot.scatter(x, y, 200, marker = '*', color = 'black')
    pyplot.show()
    
def main():
    data = readFile('collisions_cyclists.txt')
    (clusters, centroids) = kmeans(data, 6, 100)
    plotClusters(clusters, data, centroids)
    
main()
