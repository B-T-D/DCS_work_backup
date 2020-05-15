
def leibniz():
    sum = 0
    term = 1
    index = 0
    while abs(term) > 1e-6:
##        print(f"term is {term} | approx pi is {sum * 4} | index {index}")
        term = (-1) ** index / (2 * index + 1)
        sum = sum + term
        index = index + 1
    pi = sum * 4
    print(index)
    return pi

pi = leibniz()
print(pi)
