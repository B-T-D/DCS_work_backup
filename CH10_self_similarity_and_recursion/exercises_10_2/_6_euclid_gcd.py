


def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


assert gcd(10, 15) == 5, f"returned {gcd(10, 15)}"
print(f"gcd(84, 20) = {gcd(84, 20)}")
