

def diagonal_below(n):
    """Takes an integer n as parameter and returns n x n grid list of lists in
    which all cells on and below the main diagonal contain a 1 and the rest
    contain 0."""
    grid = []
    for r in range(n):
        row = []
        for c in range(n):
            if c <= r:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid


correct_n5 = [[1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0],
              [1, 1, 1, 0, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1]]

n = 5
grid = diagonal_below(n)
assert grid == correct_n5, f"fail, grid was {grid}"
