

def justone(a, b):
    """Returns True if exactly one (but not both) of numbers a or b is 10,
    and False otherwise."""
##    if a == 10 and b != 10 or a != 10 and b == 10:
##        return True
##    else:
##        return
    return True if a == 10 and b != 10 or a != 10 and b == 10 else False

def sol_man(a, b):
    return (a == 10 and b != 10) or (a != 10 and b == 10)    


tuples = [(0, 0), (10, 0), (0, 10), (10, 10)]

for tuple in tuples:
    a, b = tuple[0], tuple[1]
    print(f"{a}, {b}")
    mine = justone(a, b)
    book = sol_man(a, b)
    print(f"mine: {mine} | book's: {book}")
    
    
