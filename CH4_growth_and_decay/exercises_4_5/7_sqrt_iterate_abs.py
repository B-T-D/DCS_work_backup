def sqrt(n):

    x = 1.0
    prev_x = 0
    while abs(x - prev_x) > 1e-15:
        prev_x = x
        x = 0.5 * (x + n / x)
    return x

print(sqrt(3672))
