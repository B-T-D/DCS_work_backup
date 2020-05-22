
def multiplication_table(n):
    """Takes (int) n as a parameter, and returns an n x n multiplication table
    as a list of lists."""

    table = []

    for r in range(n):
        row = []
        for c in range(n):
            row.append((r + 1) * (c + 1))
        table.append(row)

    return table


correct_4x4 = [[1, 2, 3, 4],
               [2, 4, 6, 8],
               [3, 6, 9, 12],
               [4, 8, 12, 16]]

n = 4
table = multiplication_table(n)
assert table == correct_4x4, f"fail, table was {table}"

n = 12
table = multiplication_table(n)
assert table[n-1][n-1] == 144
