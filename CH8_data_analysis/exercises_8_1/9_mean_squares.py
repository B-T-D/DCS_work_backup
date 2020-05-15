
def mean_squares(data):
    """Returns arithmetic mean of the squares of the numbers in the list data."""
    sum = 0
    for d in data: # square and sum elements in data
        sum += d ** 2
    return sum / len(data)

assert mean_squares([2, 3, 4, 5]) == 13.5, f"returned {mean_squares([4, 9, 16, 25])}"
