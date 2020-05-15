#!/usr/bin/env python3

BLOCKED = 0  # site is blocked 
OPEN = 1     # site is open and not visited
VISITED = 2  # site is open and already visited

def dfs(grid, source, dest):
    """Perform a depth-first search on a grid to determine if there
       is a path between a source and destination.

    Parameters:
        grid: a 2D grid (list of lists)
        source: a (row, column) tuple to start from
        dest: a (row, column) tuple to reach

    Return value: Boolean indicating whether destination was reached
    """
       
    (row, col) = source
    rows = len(grid)
    columns = len(grid[0])
    
    if (row < 0) or (row >= rows) \
      or (col < 0) or (col >= columns) \
      or (grid[row][col] == BLOCKED) \
      or (grid[row][col] == VISITED):    # dead end (base case)
        return False                     #   so return False
        
    if source == dest:                   # dest found (base case)
        return True                      #   so return True
        
    grid[row][col] = VISITED             # visit this cell
        
    if dfs(grid, (row, col + 1), dest):  # search east
        return True                      #  and return if dest found
    if dfs(grid, (row + 1, col), dest):  # else search south
        return True                      #  and return if dest found
    if dfs(grid, (row, col - 1), dest):  # else search west
        return True                      #  and return if dest found
    if dfs(grid, (row - 1, col), dest):  # else search north
        return True                      #  and return if dest found

    return False                         # destination was not found

def main():
    grid = [[BLOCKED, OPEN, BLOCKED, OPEN, OPEN],
        [OPEN, OPEN, BLOCKED, OPEN, OPEN],
        [BLOCKED, OPEN, OPEN, BLOCKED, OPEN],
        [OPEN, OPEN, BLOCKED, OPEN, BLOCKED],
        [OPEN, OPEN, OPEN, OPEN, BLOCKED]]
    
    result = dfs(grid, (1, 1), (3, 0))
    print(result)
    
main()
