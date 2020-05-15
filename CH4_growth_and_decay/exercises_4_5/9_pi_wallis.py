import time, math

def wallis(terms):
    """Approximates pi using the Wallis product."""

    # Make pairs
    pairs = []
    for i in range(1, terms, 2):
        pairs.append((i, i + 1))
##    print(pairs)
    product = 2
    for pair in pairs:
        numerator = 2 * (pairs.index(pair) + 1)
##        print(numerator)
        denominators = (pair[0], (pair[1] + 1))
##        print(denominators)
        product = product * (numerator / denominators[0]) # multiply in the fraction created for the first memeber of the pair
        product = product * (numerator / denominators[1]) # Second member of the pair. Different denominator, same numerator.
    pi = product
    return pi

def sol_man(terms):
    pairs = terms / 2 # (The number of pairs, not the pairs themselves)
    product = 1
    for i in range(int(pairs)):
        first = (2 * (i + 1)) / (2 * i + 1)
        second = (2 * (i + 1)) / (2 * i + 3)
        product = product * first * second
    pi = product * 2
    return pi



iterations = 1000
math_mod_pi = math.pi

starttime_mine = time.time()
pi = wallis(iterations)
endtime_mine = time.time()
runtime_mine = endtime_mine - starttime_mine
error = abs(math_mod_pi - pi)
print(f"mine ran in {runtime_mine} and was off by {error}")
print(pi)

print("-----")

start = time.time()
pi = sol_man(iterations)
end = time.time()
run = end - start
error = abs(math_mod_pi - pi)
print(f"book's ran in {run} and was off by {error}")
print(pi)


