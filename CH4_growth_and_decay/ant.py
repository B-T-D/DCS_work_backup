def ant(n):
    """Simulates the "ant on a rubber rope" problem. The rope is initially
    1m long and the ant walks 10 cm each minute. The rope is lengthened by an
    additional 1M at the end of each minute, with the ant riding along.

    Args:
        n (int): Number of minutes the ant walks

    Return:
        (float): Fraction of the rope traveled by the ant in n minutes.
    """

    total = 0
    for number in range(1, n + 1):
        total = total + (1 / number)
    return total / 10 


def reach_end():
    """Returns the number of minutes after which the ant will first have
    walked the full length of the rope."""

    rope_walked = 0
    n = 0
    while rope_walked < 1:
        rope_walked = ant(n)
        n += 1
    return n

    # Returns 12368 as the solution. 
        

try_list = [1, 10000, 25000, 100000]
for n in try_list:
    print(f"{n} minutes:\n\t{ant(n)}")

print(reach_end())
