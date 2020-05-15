def leibniz(terms):
    """Computes a partial sum of the Leibniz series.

    Args:
        terms (int): The number of terms to add

    Return:
        (float): The sum of the given number of terms.
    """

    sum = 0
    for i in range(terms):
        sum = sum + (-1) ** i / (2 * i + 1)
    pi = sum * 4
    return pi

for i in range(500):
    print(f"i = {i} | {leibniz(i)}")

i = 1000000
print(f"i = {i} | {leibniz(i)}")

i = 10000000
print(f"i = {i} | {leibniz(i)}")

i = int(1e8)
print(f"i = {i} | {leibniz(i)}")


