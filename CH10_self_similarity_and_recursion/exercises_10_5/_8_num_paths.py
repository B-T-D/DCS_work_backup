import math

def num_paths(n, row, column):
    steps = math.sqrt((row - (n - 1)) ** 2) + math.sqrt((column - (n - 1)) ** 2)
    if steps <= 2:
        return steps
    return steps + num_paths(n - 1, row, column)

def sol_man(n, row, column):
    if (row > n - 1) or (column > n - 1):
        return 0
    if (row, column) == (n - 1, n - 1):
        # This is saying from 2, 2 to itself would be one path instead of zero
        return 1
    return sol_man(n, row + 1, column) + sol_man(n, row, column + 1)
    # Think this might be broken, unless I'm misunderstanding the exercise.
        # or mis-typed. Appears to recurse infinitely. 

actual = num_paths(n=3, row=0, column=0)
expected = 6
assert actual == expected, f"actual {actual}, expected {expected}"

actual = num_paths(n=3, row=2, column=1)
expected = 1
assert actual == expected, f"actual {actual}, expected {expected}"

actual = num_paths(n=3, row=1, column=2)
expected = 1
assert actual == expected, f"actual {actual}, expected {expected}"
##assert sol_man(3, 1, 2) == actual == expected, f"actual {actual}, sol_man {sol_man(3, 1, 2)}, expected {expected}"

actual = num_paths(n=3, row=1, column=1)
expected = 2
assert actual == expected, f"actual {actual}, expected {expected}"

# no paths if a single square
actual = num_paths(n=1, row=0, column=0)
expected = 0
assert actual == expected, f"actual {actual}, expected {expected}"


actual = num_paths(16, 0, 0)
print(actual)
print(sol_man(16, 0, 0))

print(num_paths(4, 0, 0))


actual = sol_man(n=3, row=0, column=0)
expected = 6
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"solman ok for 3, 0, 0")

actual = sol_man(n=3, row=2, column=1)
expected = 1
assert actual == expected, f"actual {actual}, expected {expected}"

actual = sol_man(n=3, row=1, column=2)
expected = 1
assert actual == expected, f"actual {actual}, expected {expected}"
##assert sol_man(3, 1, 2) == actual == expected, f"actual {actual}, sol_man {sol_man(3, 1, 2)}, expected {expected}"

actual = sol_man(n=3, row=1, column=1)
expected = 2
assert actual == expected, f"actual {actual}, expected {expected}"

# no paths if a single square
actual = sol_man(n=1, row=0, column=0)
expected = 0
assert actual == expected, f"actual {actual}, expected {expected}"

