import math

def viete(terms):
    denominator = 0
    product = 2
    for i in range(1, terms):
        denominator = math.sqrt(2 + denominator)
        product = product * (2 / denominator)
    return product

def sol_man(terms):
    product = 2
    term = 0
    for i in range(1, terms + 1):
        term = math.sqrt(2 + term)
        product = product * 2 / term
    pi = product
    return pi

pi = viete(1000)
print(pi)

pi = sol_man(1000)
print(pi)
