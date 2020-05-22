
def search_grid(grid, target):
    """
    Args:
        grid (list): List of lists representing a grid
        target (same type as grid elements): Value to search for

    Returns:
        (tuple): (row, column) where the value first appears in the grid,
            else (-1, -1) if target doesn't appear in grid.
    """
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == target:
                return r, c
    return -1, -1

test_grid = [[1, 2, 3],
             [4, 698, 5],
             [7, 8, 9]]
target = 698
correct_gridpos = (1, 1) # row 2 column 2
returned = search_grid(test_grid, target)
assert returned == correct_gridpos, f"fail, returned {returned}"
print(test_grid[returned[0]][returned[1]])
