
def print_grid(grid):
    """Prints the content of a list of lists, with each row printed on
    its own line."""
    rows = len(grid)
    columns = len(grid[0])
    for r in range(rows):
        for c in range(columns):
            print(grid[r][c], end = ' ')
        print()

grid = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

print_grid(grid)
