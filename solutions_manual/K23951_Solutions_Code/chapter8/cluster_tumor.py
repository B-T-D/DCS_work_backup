#!/usr/bin/env python3

import random
import math

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
    pass
    
def main():
    data, diagnosis = readFile('breast-cancer-wisconsin.csv')
    clusters, centroids = kmeans(data, 2, 10)
    for clusterIndex in range(2):
        count = {2: 0, 4: 0}
        for dataIndex in clusters[clusterIndex]:
            count[diagnosis[dataIndex]] = count[diagnosis[dataIndex]] + 1
        print('Cluster', clusterIndex)
        print('  benign:', count[2], 'malignant:', count[4])

main()
