import random

def avg_test(n):
    """Tests the hard-coded PRNG algorithm to confirm the average of its outputs
    is about 0.5.

    Args:
        n (int): Number of PRNs to generate for the test sequence.
    """

    sequence = []
    for i in range(n):
        r = random.random()
        sequence.append(r)

    sum = 0
    for number in sequence:
        sum += number
    mean = sum / n
    return mean
    # Think the book wants us to not know sum() yet

print("n    | mean  ")
for i in range(6):
    n = 10 ** i
    mean = avg_test(n)
    print(f"{n}   | {mean}")
        
