

def f(a, b):
    """Takes two integers as args and returns their sum if they're not equal,
    and their product if they are."""

    return a + b if a != b else a * b

print(f(2,2))
print(f(2,3))
print(f(3,3))
