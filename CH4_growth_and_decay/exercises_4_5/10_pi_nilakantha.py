import time, math

def nilakantha(terms):
    """Approximates pi using the Nilakantha series."""
    sum = 3
    denom_start = 2
    for i in range(terms):
        denominator = denom_start * (denom_start + 1) * (denom_start + 2)
        denominator = denominator * (-1) ** i
        denom_start += 2
        sum = sum + 4 / denominator
    pi = sum
    return pi

def sol_man(terms):
    # Book's is detectably faster once iterations are above around 100k.
    #   ...But then book's came in slower at 1e6 iterations. May be other stuff
    #   influencing it and/or i may not be measuring it optimally.
    # Book again came in slower at 1e7, slower again at 1e8.
    sum = 3
    for i in range(1, terms + 1):
        sum = sum + (-1)**(i-1) * 4 / ((2*i) * (2 * i + 1) * (2 * i + 2))
    pi = sum
    return pi

iterations = 1000000
mm_pi = math.pi

# Both mine and book's appear to run in linear time. Based on manually trying
#   iterations = powers of 10 up to 1e8. The runtime was increasing by a power of
#   10 when iterations increased by power of 10. 

start = time.time()
pi = nilakantha(iterations)
end = time.time()
run = end - start
error = abs(mm_pi - pi)
print(f"mine ran in {run} and was off by {error}")
print(pi)

print('-------')

start = time.time()
pi = sol_man(iterations)
end = time.time()
run = end - start
error = abs(mm_pi - pi)
print(f"book's ran in {run} and was off by {error}")
print(pi)
