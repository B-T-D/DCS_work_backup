import copy

def make_grid(rows, columns):
    """Returns a list of lists representing a rows x columns grid, for use in
    Game of Life."""

    grid = []
    for r in range(rows):
        row = [DEAD] * columns
        grid.append(row)
    return grid

def initialize(grid, coordinates):
    """Set a given list of coordinates to 1 in the grid. I.e. set the starting
    alive cells.

    Args:
        grid (list): A grid of values for a cellular automaton
        coordinates(list): List of coordinates to set to 1

    Returns:
        None
    """
    for r, c in coordinates:
        grid[r][c] = ALIVE

def neighborhood(grid, row, column):
    """Returns number of live neighbors of the cell at row, column in grid."""

    offsets = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),            (0, 1),
                (1, -1), (1, 0), (1, 1)]
    rows = len(grid)
    columns = len(grid[0])
    count = 0
    for offset in offsets:
        r = row + offset[0]
        c = column + offset[1]
        if (r >= 0 and r < rows) and (c >= 0 and c < columns):
            if grid[r][c] == ALIVE:
                count = count + 1
    return count

def life(rows, columns, generations, initial_cells):
    """Simulates the Game of Life for the given number of generations,
    starting with the given live cells initial_cells.

    Args:
        rows (int): Number of rows in the grid
        columns(int): Number of columns in the grid
        generations (int): Number of generations to simulate
        initial_cells (list): List of (row, column) tuples indicating positions
            of the initially alive cells

    Return value:
        (list): Final configuration of cells in a grid
    """

    grid = make_grid(rows, columns)
    initialize(grid, initial_cells)
    for g in range(generations):
        new_grid = copy.deepcopy(grid)
        for r in range(rows):
            for c in range(columns):
                neighbors = neighborhood(grid, r, c)
                if grid[r][c] == ALIVE and neighbors < 2: # rule 1
                    new_grid[r][c] = DEAD
                elif grid[r][c] == ALIVE and neighbors > 3: # rule 3
                    new_grid[r][c] = DEAD
                elif grid[r][c] == DEAD and neighbors == 3: # rule 4
                    new_grid[r][c] = ALIVE
        grid = new_grid
    return grid

ALIVE = 1
DEAD = 0

grid = make_grid(10, 10)
print(grid)
print(len(grid))
for row in grid:
    print(len(row))

initial_cells = [(1, 3), (2, 3), (3, 3), (3, 2), (2, 1)]
generations = 5
grid = life(10, 10, generations, initial_cells)
print(grid)
