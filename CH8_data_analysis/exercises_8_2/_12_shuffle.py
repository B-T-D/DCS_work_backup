import random
from _5_swap import swap

def shuffle(data):
    """Shuffles items in the list data in place, using the prior ex swap()
    function.

    Function should perform 100 swaps regardless of number of list elements(?).
    """
    for i in range(100):
        start = random.randint(0, len(data) - 1)
        end = random.randint(start + 1, len(data) - 1) # start + 1 to avoid a non-swap where both indices are the same
        swap(data, start, end)
    
string = "Write a function shuffle(data) that shuffles the items in the list \
named data in place, without using the shuffle function from the random module."

data = string.split()
print(data)
shuffle(data)
print(data)
