import copy

ALIVE = 1
DEAD = 0

def emptyGrid(rows, columns):
    """Create a rows x columns grid of zeros.

    Parameters:
        rows: the number of rows in the grid
        columns: the number of columns in the grid

    Return value: a list of ROWS lists of COLUMNS zeros
    """
    
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
        r = (row + offset[0]) % rows
        c = (column + offset[1]) % columns
        if grid[r][c] == ALIVE:
            count = count + 1
    return count

def test_wraparound():
    """Confirms that wraparound works correctly."""
    # set up the 7x7, square (6, 6) thing, and intialize all neighbors as alive.
    #   That means that with proper wraparound, neighborhood returns 8, all 8
    #   neighbors.

    grid = emptyGrid(7, 7) # start with a blank 7x7

    alive = [(0, 0), (0, 5), (0, 6), (5, 0), (5, 5), (5, 6), (6, 0), (6, 5)]

    initialize(grid, alive)

    count = neighborhood(grid, 6, 6) # return alive neighbors of 6, 0
    for row in grid:
        print(row)
    assert count == 8, f"fail, neighborhood returned {count}"

    
test_wraparound()
