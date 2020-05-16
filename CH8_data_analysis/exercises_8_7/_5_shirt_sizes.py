"""Given 100 customers' torso length and chest measurements, use k-means
clustering to cluster the customers into three groups: S, M, and L."""

from measurements import measurements
import kmeans as km
from matplotlib import pyplot

def plot_size_clusters(clusters, data, centroids):
    """Plot shirt size clusters with chest on x axis, torso length (~height) on
    y axis."""
    colors = ['blue', 'red', 'green']
    for cluster_index in range(len(clusters)):
        x = []
        y = []
        for data_index in clusters[cluster_index]:
            x.append(data[data_index][0])
            y.append(data[data_index][1])
        pyplot.scatter(x, y, 10, color = colors[cluster_index])

    x = []
    y = []
    for centroid in centroids:
        x.append(centroid[0])
        y.append(centroid[1])
    pyplot.scatter(x, y, 200, marker = '*', color = 'black')
    pyplot.xlabel('Chest size')
    pyplot.ylabel('Torso length')
    pyplot.show()



k = 3 # 3 groups, small medium large

data = measurements

clusters, centroids = km.kmeans(data, k, iterations=10)
print(clusters)
print(centroids)
plot_size_clusters(clusters, data, centroids)

