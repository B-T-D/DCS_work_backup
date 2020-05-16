import _1_to_2_distance_and_centroid as e2
import random
from matplotlib import pyplot

def read_file(filename):
    """Read locations of 2012 bicycle accidents in Manhattan into a
    list of tuples.

    Args:
        filename (str): Name of the txt file with the data formatted as
            expected.

    Returns:
        (list): List of tuples with (longitude, latitude)

    """
    input_file = open(filename, 'r', encoding='utf-8')
    header = input_file.readline() # read past the header line
    data = []
    for line in input_file:
        row = line.split('\t')
        borough = int(row[0])
        year = int(row[2])
        if (borough == 1) and (year == 2012): # 1 is the manhattan 'borocode'
            longitude = float(row[4])
            latitude = float(row[5])
            data.append( (longitude, latitude) )
    input_file.close()
    return data

def kmeans(data, k, iterations):
    """Cluster data into k clusters using the given number of iterations
    of the k-means clustering algorithm.

    Args:
        data (list): A list of points
        k (int): Number of desired clusters
        iterations (int): Number of iterations of the algorithm

    Returns:
        (tuple): Tuple containing the list of clusters and the list of
            centroids. Each cluster is represented by a list of indices
            of the points assigned to that cluster.
    """
    n = len(data)
    centroids = random.sample(data, k)

    for step in range(iterations):
        clusters = []
        for i in range(k):
            clusters.append([]) # a list of empty lists
        for data_index in range(n):
            min_index = 0
            for cluster_index in range(1, k):
                dist = e2.distance(centroids[cluster_index], data[data_index])
                if dist < e2.distance(centroids[min_index], data[data_index]):
                    min_index = cluster_index
            clusters[min_index].append(data_index) # this is where it finishes reassigning
                    # points between clusters. 

        for cluster_index in range(k): # update to new centroids at end of each iteration
            centroids[cluster_index] = e2.centroid(clusters[cluster_index], data)
    return clusters, centroids

def kmeans2(data, k):
    """Iterates until the list of clusters stops changing. Rather than taking iterations
    as an argument."""

    n = len(data)
    centroids = random.sample(data, k)
    prev_clusters = None
    clusters = []
        # should still cause the while condition to be False first time it's evaluated
    iterations = 0
    while clusters != prev_clusters:
        prev_clusters = clusters
        clusters = []
        for i in range(k):
            clusters.append([])
        for data_index in range(n):
            min_index = 0
            for cluster_index in range(1, k):
                dist = e2.distance(centroids[cluster_index], data[data_index])
                if dist < e2.distance(centroids[min_index], data[data_index]):
                    min_index = cluster_index
            clusters[min_index].append(data_index)

        for cluster_index in range(k):
            centroids[cluster_index] = e2.centroid(clusters[cluster_index], data)
        iterations += 1
    print(f"took {iterations} iterations to stabilize")
    return clusters, centroids
    

    
    

def plot_clusters(clusters, data, centroids):
    """Plot clusters and centroids in unique colors.
    Args:
        clusters (list): List of k lists of data indices
        data (list): List of points
        centroids (list): LIst of k centroid points

    Returns:
        None
    """
    colors = ['blue', 'red', 'yellow', 'green', 'purple', 'orange']
    for cluster_index in range(len(clusters)):  # plot clusters of points
        x = []
        y = []
        for data_index in clusters[cluster_index]:
            x.append(data[data_index][0])
            y.append(data[data_index][1])
        pyplot.scatter(x, y, 10, color = colors[cluster_index])

    x = []
    y = []
    for centroid in centroids: # plot centroids (on same pyplot object since before the .show() call)
        x.append(centroid[0])
        y.append(centroid[1])
    pyplot.scatter(x, y, 200, marker = '*', color = 'black') # asterisk will display as a 5 pointed star
    pyplot.show()

def main():
    filename = 'collisions_cyclists.txt'
    data = read_file(filename)
    k = 6
    iterations = 100 
##    clusters, centroids = kmeans(data, k, iterations)
    clusters, centroids = kmeans2(data, k)
    plot_clusters(clusters, data, centroids)

if __name__ == '__main__':
    main()
