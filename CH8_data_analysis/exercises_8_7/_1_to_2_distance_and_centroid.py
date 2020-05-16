import math
import random

def distance(p, q):
    """Returns the Euclidean distance between k-dimensional points p and q, each
    of which is represented by a tuple with length k.
    """
    assert len(p) == len(q), f"Points in distance(p, q) function don't have same \
number of elements."
    k = len(p)
    sum = 0 # accumulator for sum of (p - q) ** 2
    for i in range(len(p)):
        sum += (p[i] - q[i]) ** 2
    return math.sqrt(sum) 
    
def simple_test(): # simple common case
    """Tests the function with two two-dimensional points."""
    p = (0, 1)
    q = (1, 1)
    correct_distance = 1
    returned_distance = distance(p, q)
    assert returned_distance == correct_distance
    print("\tok simple_test()")

def larger_test(): # more complex common case
    """Tests the function with the 6 dimensional points in book at 411."""
    p1 = (85, 92, 45, 27, 31, 0.0)
    p2 = (85, 64, 59, 32, 23, 0.0)
    # p3 not copied, seems YAGNI
    correct_distance = 32.7 # book rounds to this
    returned_distance = distance(p1, p2)
    assert round(returned_distance, 1) == correct_distance
    print("\tok larger_test()")

def test_distance():
    print("test_distance():")
    simple_test()
    larger_test()
    print("---")

def centroid(cluster, data):
    """Computes the centroid of the given cluster, which is a list of indixes of
    points in data.

    Returns a randomly chosen point in data if the cluster is empty.
    Args:
        cluster (list): List of indices of points in data.
        data (list): A list of k-element tuples (e.g. a 3 dimensional point is represented
            by a three-element tuple.

    Returns:
        (tuple): Tuple containing k-elements for a k-dimensional point in data.
    """
    k = len(data[0]) # number of elements in first tuple should equal k
    for d in data:
        assert len(d) == k, "bad points elements in centroid()" # every tuple should have k elements, if not something is wrong

    n = len(cluster) 
    if n == 0:
        return random.choice(data)

    centroid = []
    for i in range(k): # Iterate each dimension-coordinate  
        sum = 0
        for data_index in cluster:
            point = data[data_index]
            sum += point[i]
        centroid.append(sum / n)
    return tuple(centroid)

def main():
    test_distance()

if __name__ == '__main__':
    main()
    
