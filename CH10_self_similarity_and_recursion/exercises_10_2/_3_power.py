def power(a, n):
    """Returns the value of a raised to the power n, using recursion and
    without using the ** operator."""
    if n == 2: # doesn't work -- recurses infinitely if n < 2
        return a * a
    return a * power(a, n - 1)

def solman(a, n):
    # Even this one recurses infinitely if n < 0, i.e. it can't do negative
    #   exponents.
    if n == 0:
        return 1
    return a * power(a, n - 1)

a = 2
n = 3
control = a ** n
returned = power(a, n)
assert returned == control, f"returned {returned}"

##assert power(2, 0) == 1, f"a ** 0  should return 1, returned {power(2, 0)} for a = 2, n = 0"
assert solman(2, 0) == 1, f"solman(2, 0) returned {solman(2, 0)}"

