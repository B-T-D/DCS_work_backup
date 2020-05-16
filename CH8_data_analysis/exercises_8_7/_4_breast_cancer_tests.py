import kmeans as km

def read_file(filename):
    """
    Returns a tuple of two lists.
    
    Args:
        filename : The specific csv file whose data this program is made for
        
    Returns:
        (tuple): (list) data, list of 9-element tuples of test results;
            (list) diagnosis, list of integers in same order as test results
    """
    data = []
    diagnosis = []
    file = open(filename, 'r')
    # it doesn't have a header row
    for line in file:
        line = line.strip('\n')
        row = line.split(',') # split by comma because 'comma separated values'
        row_data = tuple([int(i) for i in row[1:-1]])
        data.append(row_data)
        diagnosis.append(int(row[-1]))
    file.close()
    return data, diagnosis

def main():
    filename = 'breast-cancer-wisconsin.csv'
    data, diagnosis = read_file(filename)
    clusters, centroids = km.kmeans(data, 2, 10) # 2 clusters, 10 iterations
    for cluster_index in range(2):
        count = {2: 0, 4: 0}
        for index in clusters[cluster_index]:
            count[diagnosis[index]] = count[diagnosis[index]] + 1
        print('Cluster', cluster_index)
        print('  benign: ', count[2], 'malignant: ', count[4]) 

if __name__ == '__main__':
    main()
