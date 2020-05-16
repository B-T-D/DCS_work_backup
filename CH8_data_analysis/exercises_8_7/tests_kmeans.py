"""Unit tests for k means related functions using unittest module."""

import unittest

import _1_to_2_distance_and_centroid as e2
import kmeans as km

class TestCentroidCommon(unittest.TestCase):
    """Common-case test for the centroid() function, using the data at
    top of 414 as (list) data."""

    data = [(0.5, 5), (1.75, 5.75), (3.5, 2), (4, 3.5), (5, 2), (7, 1)]
    k = len(data[0])
    for d in data:
        assert len(d) == k, "Bad points-tuples in data in unittest TestCentroidCommon."
        

    def test_return_initial_centroid(self):
        """Does it return the random initial centroid as a randomly chosen
        actual-point in data?"""
        cluster = []
        centroid = e2.centroid(cluster, self.data)

        self.assertIs(tuple, type(centroid))
        self.assertEqual(self.k, len(centroid))
        self.assertIn(centroid, self.data) # Confirm the point is one from data

    def test_return_computed_centroid(self):
        """Does it return a computed centroid after starting with a cluster?

        Values are from 412 initial clusters for red random choice centroid (0.5, 5), blue
        rando centroid (7, 1).
        """
        cluster_red = [0, 1, 3] # (0.5, 5), (1.75, 5.75), (4, 3.5)
        correct_centroid = (2.08, 4.75) # book at 412-13 rounds to those

        centroid = e2.centroid(cluster_red, self.data)
        self.assertIs(tuple, type(centroid))
        rounded_centroid = tuple([round(element, 2) for element in centroid])
        self.assertEqual(correct_centroid, rounded_centroid)

    def test_many_dimensions(self):
        """Does it work for a point that has several dimensions more than just x and y?"""
        data = [(85, 92, 45, 27, 31, 0.0), (85, 64, 59, 32, 23, 0.0), (86, 54, 33, 16, 54, 0.0)]
        cluster = [0, 1, 2] # just using all points rather than only two or dealing with making up more 
        # page 411 three points
        k = len(data[0])
        for d in data:
            assert len(d) == k
        centroid = e2.centroid(cluster, data)
        self.assertIs(tuple, type(centroid))
        self.assertEqual(k, len(centroid))

        # for empty cluster
        cluster = []
        centroid = e2.centroid(cluster, data)
        self.assertIn(centroid, data)
        
class TestKmeansCommon(unittest.TestCase):
    """
    """
    data = [(0.5, 5), (1.75, 5.75), (3.5, 2), (4, 3.5), (5, 2), (7, 1)]
    m = len(data[0]) # m is number of dimensions
    for d in data:
        assert len(d) == m, "Bad points-tuples in data in unittest TestCentroidCommon."

    def test_kmeans_basics(self):
        """Does it return a tuple of lists?"""
        k = 2
        iterations = 3
        returned_obj = km.kmeans(self.data, k, iterations)
        self.assertIs(tuple, type(returned_obj))
        for i in range(len(returned_obj)): # is each element in the tuple a list?
            self.assertIs(list, type(returned_obj[i]))

    def test_against_book_control(self):
        """Do clusters and centroids returned by kmeans match the example ones in book
        circa 414?"""
        # imperfect, can theoretically fail from RNG, IMU even at high values of iterations
        expected_clusters = [[0, 1], [2, 3, 4, 5]]
        expected_centroids = [(1.125, 5.375), (4.875, 2.125)]
        result = km.kmeans(self.data, k=2, iterations=1000)
        print(result)
        returned_clusters = result[0]
        returned_centroids = result[1]
        # compare both possible orderings because they come back in random order (i.e. varies which cluster first)
        try:
            self.assertEqual(expected_clusters[0], returned_clusters[0])
            self.assertEqual(expected_clusters[1], returned_clusters[1])
        except AssertionError:
            self.assertEqual(expected_clusters[1], returned_clusters[0])
            self.assertEqual(expected_clusters[0], returned_clusters[1])
        try:
            self.assertEqual(expected_centroids[0], returned_centroids[0])
            self.assertEqual(expected_centroids[1], returned_centroids[1])
        except AssertionError:
            self.assertEqual(expected_centroids[1], returned_centroids[0])
            self.assertEqual(expected_centroids[0], returned_centroids[1])
        

        

if __name__ == '__main__':
    unittest.main()
                     
    
