# Book's way was different and IMO less elegant

import random

def max_3(a, b, c):
    """Returns the max value of a, b, c."""

    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

    # Mine could be changed pretty easily into one that could recurse over
    #   arbitrarily large list of numbers not just 3. 

def sol_man(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif b >= c:
        return b
    else:
        return c

# Generate some random sets of 3 numbers to pass as args:
lists = []
for i in range(10):
    sublist = []
    for i in range(3):
        sublist.append(random.randint(0, 100))
    lists.append(sublist)
lists.append([5, 5, 5])

print("a   | b   | c   | max")
for list in lists:
    print(f"{list[0]} | {list[1]} | {list[2]} | {max_3(list[0], list[1], list[2])}")
    
print('-------book-------')
print("a   | b   | c   | max")
for list in lists:
    print(f"{list[0]} | {list[1]} | {list[2]} | {sol_man(list[0], list[1], list[2])}")
