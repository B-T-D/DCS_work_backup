
def eratosthenes(n):
    """Return a list of all prime numbers less than or equal to n, using the
    sieve of Eratosthenes algorithm."""
    primes = [True for i in range(n)]
    primes[0] = False
    primes[1] = False

    
    for i in range(2, n):
        if primes[i] == True:
            j = i + i
            while j < n:
                primes[j] = False
                j += i
    returned_primes = []
    for i in range(len(primes)):
        if primes[i] == True:
            returned_primes.append(i)
    return returned_primes

def solman(n):
    prime = [False, False] + [True] * (n - 1)
    for index in range(2, n // 2):
        if prime[index]:
            for multiple in range(2 * index, n + 1, index): # sets the step to i--so the builtin increments to the next multiple without needing a while loop
                prime[multiple] = False
    primes = []
    for index in range(2, n + 1):
        if prime[index]:
             primes.append(index)
    return primes

n = 12
expected = [2, 3, 5, 7, 11]
actual = eratosthenes(n)
assert actual == expected, f"actual {actual}, expected {expected}"

print(solman(20))

##print(eratosthenes(100))
