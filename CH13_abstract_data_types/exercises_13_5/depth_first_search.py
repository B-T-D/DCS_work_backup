#!/usr/bin/env python3

import turtle
import random
from stack_additions import Stack

BLOCKED = 0  # site is blocked 
OPEN = 1     # site is open and not visited
VISITED = 2  # site is open and already visited

SCALE = 16   # drawing scale
    
def drawSquare(pos, color, tortoise):
    """Draws one square in the given color at the
       given position in the grid.
       
    Parameters: 
        pos: a (row, column) tuple
        color: a color string
        tortoise: a Turtle object
        
    Return value: None
    """
    
    (row, column) = pos
    screen = tortoise.getscreen()
    rows = int(screen.canvheight / screen.yscale)
    row = rows - row - 1
    tortoise.shape(color)
    tortoise.up()
    tortoise.goto(column, row + 1)
    tortoise.stamp()
    
def drawGrid(grid, rows, columns, tortoise):
    """Draws a grid using turtle graphics.
       
    Parameters: 
        grid: the 2D grid
        rows: the number of rows in the grid
        columns: the number of columns in the grid
        tortoise: a Turtle object
        
    Return value: None
    """
    
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == BLOCKED:
                drawSquare((row, col), 'black', tortoise)
            else:
                drawSquare((row, col), 'white', tortoise)
        
def createSquares(screen, colors):
    """Creates square shapes in the given colors to be used
       as turtle graphics stamps in a cellular automata.
       
    Parameters: 
        screen: a Screen object
        colors: a list of color strings
        
    Return value: None
    """
    
    square = ((0, 0), (0, SCALE), (SCALE, SCALE), (SCALE, 0))
    for color in colors:
        squareShape = turtle.Shape('compound')
        squareShape.addcomponent(square, color, 'gray')
        screen.register_shape(color, squareShape)

def randomGrid(rows, columns, p):
    """Creates a random grid with vacancy probability p.
    
    Parameters: 
        rows: the number of rows in the grid
        columns: the number of columns in the grid
        p: the vacancy probability
        
    Return value: a random grid with vacancy probability p
    """

    grid = []
    for r in range(rows):
        row = []
        for c in range(columns):
            if random.random() < p:
                row.append(OPEN)
            else:
                row.append(BLOCKED)
        grid.append(row)
    return grid
    
def dfs(grid, source, dest, tortoise):
    """Perform a depth first search on a grid to determine if there
       is a path between a source and destination.

    Parameters:
        grid (list): a 2D grid (list of lists)
        source (tuple): a (row, column) tuple to start from
        dest (tuple): a (row, column) tuple to reach
        tortoise (Turtle): a Turtle object

    Return value: Boolean indicating whether destination was reached
    """

    stack = Stack() # a stack of locations
    stack.push(source)

    rows = len(grid)
    columns = len(grid[0])
    
    while not stack.is_empty():
        position = stack.pop()
        row, col = position
        # first check if position is already the destination:
        if position == dest:
            return True
        # check if this position can be visited
        if not ((row < 0) or (row >= rows) or (col < 0) or (col >= columns) or \
           (grid[row][col] == BLOCKED) or (grid[row][col] == VISITED)):
            # if so mark it visited...
                grid[row][col] = VISITED
                drawSquare((row, col), 'blue', tortoise)
            #...and add its four neighbors to the stack.
                # should work to add them by simply adding/subtracting 1 from the coords
                neighbors = [(row - 1, col), # north
                             (row + 1, col), # south
                             (row, col - 1), # east
                             (row, col + 1)] # west
                for n in neighbors:
##                    drawSquare(n, 'lightblue', tortoise)
                    stack.push(n)

    return False
                    
                    
        
##        print(position)
##        
##    (row, col) = source
##    
##    
##    if (row < 0) or (row >= rows) or (col < 0) or (col >= columns) or \
##       (grid[row][col] == BLOCKED) or (grid[row][col] == VISITED):
##        return False                               # dead end (base case) so return False
##        
##    if source == dest:                             # dest found (base case)
##        return True                                #   so return True
##        
##    grid[row][col] = VISITED                       # visit this cell
##    drawSquare((row, col), 'blue', tortoise)
##
##    ## this algo searches east first--that's why it seems to guess
##    #   suspiciously well when source is (1, 1) and dest is (18, 18)
##    
##    if dfs(grid, (row, col + 1), dest, tortoise):  # search east
##        return True                                #  and return if dest found
##    if dfs(grid, (row + 1, col), dest, tortoise):  # else search south
##        return True                                #  and return if dest found
##    if dfs(grid, (row, col - 1), dest, tortoise):  # else search west
##        return True                                #  and return if dest found
##    if dfs(grid, (row - 1, col), dest, tortoise):  # else search north
##        return True                                #  and return if dest found
##
##    drawSquare((row, col), 'lightblue', tortoise)
##    return False                                   # destination was not found
    
    
def searchPath(grid, source, dest):
    """Set up turtle graphics to draw the grid and then call dfs to
       find a path between source and dest.
       
    Parameters:
        grid: a 2D grid (list of lists)
        source: a (row, column) tuple to start from
        dest: a (row, column) to tuple to reach

    Return value: None
    """
    
    rows = len(grid)
    columns = len(grid[0])

    tortoise = turtle.Turtle()
    screen = tortoise.getscreen()
    screen.setup(columns * SCALE + 20, rows * SCALE + 20)
    screen.setworldcoordinates(0, 0, columns, rows)
    screen.tracer(10)
    tortoise.hideturtle()
    createSquares(screen, ['black', 'white', 'blue', 'lightblue', 'red', 'green'])
    
    drawGrid(grid, rows, columns, tortoise)
    drawSquare(source, 'green', tortoise)
    drawSquare(dest, 'red', tortoise)
    
    success = dfs(grid, source, dest, tortoise)
    if success:
        print('A path was found!')
    else:
        print('A path was not found.')

    screen.update()
##    screen.exitonclick()

def main():
    """
    COLORS:
        light blue = visited and backtracked-from, not part of path to dest
        white = open
        black = blocked
        blue = the path from source to dest
        red = dest
        green = source--but gets overwritten by blue or light blue
    """
##    grid = [[BLOCKED, OPEN, BLOCKED, OPEN, OPEN],   # example from the text
##            [OPEN, OPEN, BLOCKED, OPEN, OPEN],
##            [BLOCKED, OPEN, OPEN, BLOCKED, OPEN],
##            [OPEN, OPEN, BLOCKED, OPEN, BLOCKED],
##            [OPEN, OPEN, OPEN, OPEN, BLOCKED]]
##    searchPath(grid, (1, 1), (3, 0))
    
    columns = 20                                    # search a larger random grid
    rows = 20
    grid = randomGrid(rows, columns, 0.75)
    grid[1][1] = OPEN
    grid[18][18] = OPEN
##    searchPath(grid, (1, 1), (18, 18)) # source is (1, 1) (near top left), destination
                                        # is (18, 18) (near bottom right)
    # It'll (the CH10 recursive version not the stack version CH13) guess very well with 1, 1 to 18, 18,
    #   because it always tries east first and then tries south. (18, 18) is east and sourth of (1, 1)
    # Won't do so well with the reverse route:
    searchPath(grid, (18, 18), (1, 1))
    
main()
