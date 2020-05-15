def mean(data):
    sum = 0
    for item in data:
        sum += item
    return sum / len(data)

def mean_squares(data):
    """Returns arithmetic mean of the squares of the numbers in the list data."""
    sum = 0
    for d in data: # square and sum elements in data
        sum += d ** 2
    return sum / len(data)

def variance(data):
    """Returns the variance of the list of numbers data."""

    return mean_squares(data) - mean(data) ** 2

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mean(data))
print(variance(data))    

    
