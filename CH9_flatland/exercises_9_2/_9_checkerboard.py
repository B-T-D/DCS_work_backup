

def checkerboard():
    """Returns 2D grid  list of lists representation of a checkerboard with
    the squares in both directions alternationging between values 'B' and
    'W'."""
    board = []
    for r in range(8):
        row = []
        if r % 2 == 0:
            for c in range(4):
                row.append('B')
                row.append('W')
        else:
            for c in range(4):
                row.append('W')
                row.append('B')
        board.append(row)
    return board

def sol_man():
    board = []
    for r in range(8):
        row = []
        for c in range(8): # he does even-odd by each square rather than by row
            if (r + c) % 2 == 1:
                row.append('B')
            else:
                row.append('W')
        board.append(row)
    return board

grid = checkerboard()
for row in grid:
    print(row)

print('\n-----\n')
grid = sol_man()
for row in grid:
    print(row)
