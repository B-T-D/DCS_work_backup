import math

def approx_pi(n):
    """Approximates pi using the Madhava of Sangamagrama series."""
    sum = 0
    for i in range(n + 1):
        term = 1 / (3 ** i * (2 * i + 1))
        sign = (-1) ** i
        term = sign * term
##        print(term)
        sum = sum + term
    pi = sum * math.sqrt(12)
    return pi


pi = approx_pi(10000)
print(pi)
