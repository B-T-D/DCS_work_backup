import random

def magic_square(n):
    """Returns an n x n magic square.
    Args:
        n (int): Odd integer.
    """
    # construct blank square:
    square = []
    for row in range(n):
        r = [0] * n
        square.append(r)
    # place 1 randomly somewhere
    row = random.randint(0, n - 1)
    column = random.randint(0, n - 1)
    square[row][column] = 1
    for number in range(2, n ** 2 + 1): # iterate through numbers in [2..n**2] until all are placed
        
        # check if down and right square is blank:
        if square[(row + 1) % n][(column + 1) % n] == 0:
            row = (row + 1) % n
            column = (column + 1) % n
            square[row][column] = number
        else: # if that square is full change row and column to be the square directly above
            row = (row - 1) % n # one up none over
            # will it always be blank if this was reached and not all nums
                # written yet?
            square[row][column] = number
    return square

square = magic_square(3)


for row in square:
    assert sum(row) == 15

for column in range(len(square[0])):
    colsum = 0
    for row in range(len(square)):
        colsum += square[row][column]
    assert colsum == 15


square = magic_square(25)
for row in square:
    print(row)

    
