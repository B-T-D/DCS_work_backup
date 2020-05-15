# Book just turns it into an integer with int(), then multiplies by 8. 

import random
import turtle

def prng(n):
    """Returns an integer in [0, n]."""

    list = []
    for i in range(n + 1):
        list.append(i)

    r = random.random()

    number = None

    for e in list:
        if r < (e + 1) / (n + 1):
            number = e
##            print(f"r: {r} | e : {e} | n: {n} | current number: {number}")
            return number
        
    return number

def test_prng_average(n, trials):
    list = []
    for i in range(n + 1):
        list.append(i)

    sequence = []
    for i in range(trials):
        number = prng(n)
        sequence.append(number)

    model_avg = sum(list) / (n + 1)
    print(f"average should be close to {model_avg}")

    return sum(sequence) / trials

def sol_man():
    number = int(random.random() * 8)
    return number

    # Will this ever return zero?

##print(test_prng_average(7, 1000))

for i in range(20):
    print(sol_man())
