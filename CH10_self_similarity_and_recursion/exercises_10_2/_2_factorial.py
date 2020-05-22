def factorial(n):
    """returns the value of n!, using recursion."""
    if n <= 1:
        return n # this is the same as returning 1. Solman does return 1
    return n * factorial(n - 1)

def solman(n):
    if n <= 1:
        return 1
    else: # why does it use an else? Confirmed it works without it
        return n * factorial(n - 1)

test_fact = 120 # 5!
n = 5
returned = factorial(n)
assert returned == 120, f"returned {returned}"

solman_return = solman(n)
assert solman_return == 120, f"returned {solman_return}"
