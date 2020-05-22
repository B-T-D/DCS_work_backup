

def diagonal(n):
    """Takes (int) n as parameter, and returns n x n grid list of lists in which
    all cells  on the main diagonal contain a 1 and the rest of the cells contain
    a 0."""
    grid = []
    c = 0
    for row in range(n):
        row = [0] * 5
        row[c] = 1
        grid.append(row)
        c += 1
    return grid

correct_n5 = [[1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1]]

n = 5
grid = diagonal(n)
assert grid == correct_n5, f"fail, grid was {grid}"
