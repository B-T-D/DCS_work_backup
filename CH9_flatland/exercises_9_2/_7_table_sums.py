def table_sum(grid):
    """Takes as a parameter a two dimensional grid list of lists and prints
    sum of each row, sum of each column, and sum of all entries."""
    print("Sum of rows:")
    for row in grid:
        print(f"\t{sum(row)}")
    print("Sum of columns:")
    for c in range(len(grid[0])):
        colsum = 0
        for row in grid:
            colsum += row[c]
        print(f"\t{colsum}")
    print("Sum of all values in table:")
    tabsum = 0
    for row in grid:
        tabsum += sum(row)
    print(f"\t{tabsum}")




test_grid = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

test_row_sums = [6, 15, 24]
test_column_sums = [12, 15, 18]
test_full_sum = 45

table_sum(test_grid)
