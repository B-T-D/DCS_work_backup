#!/usr/bin/env python3

import copy

ALIVE = 1
DEAD = 0

def makeGrid(rows, columns):
    """Create a rows x columns grid of zeros.

    Parameters:
        rows: the number of rows in the grid
        columns: the number of columns in the grid

    Return value: a list of ROWS lists of COLUMNS zeros
    """

    grid = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(DEAD)
        grid.append(row)
    return grid
    
def initialize(grid, coordinates):
    """Set a given list of coordinates to 1 in the grid.

    Parameters:
        grid: a grid of values for a cellular automaton
        coordinates: a list of coordinates

    Return value: None
    """

    for (r, c) in coordinates:
        grid[r][c] = ALIVE

def neighborhood(grid, row, column):
    """Finds the number of live neighbors of the cell in the
       given row and column.
    
    Parameters:
        grid: a two-dimensional grid of cells
        row: the row index of a cell
        column: the column index of a cell
        
    Return value:
        the number of live neighbors of the cell at (row, column)
    """
    
    offsets = [ (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)   ]
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
    
def life(rows, columns, generations, initialCells):
    """Simulates the Game of Life for the given number of
       generations, starting with the given live cells.
    
    Parameters:
        rows: the number of rows in the grid
        columns: the number of columns in the grid
        generations: the number of generations to simulate
        initialCells: a list of (row, column) tuples indicating
                      the positions of the initially alive cells
        
    Return value:
        the final configuration of cells in a grid
    """
    
    grid = makeGrid(rows, columns)
    initialize(grid, initialCells)
    for g in range(generations):
        newGrid = copy.deepcopy(grid)
        for r in range(rows):
            for c in range(columns):
                neighbors = neighborhood(grid, r, c)
                if grid[r][c] == ALIVE and neighbors < 2:     # rule 1
                    newGrid[r][c] = DEAD
                elif grid[r][c] == ALIVE and neighbors > 3:   # rule 3
                    newGrid[r][c] = DEAD
                elif grid[r][c] == DEAD and neighbors == 3:   # rule 4
                    newGrid[r][c] = ALIVE
        grid = newGrid
    return grid
    
def main():
    initialConfiguration = [(1, 3), (2, 3), (3, 3), (3, 2), (2, 1)]
    finalGrid = life(10, 10, 15, initialConfiguration)
    print(finalGrid)
    
main()
