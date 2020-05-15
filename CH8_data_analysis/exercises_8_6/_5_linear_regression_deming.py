import math

def linear_regression_deming(x, y):
    """
    Computes Deming regression line values for lists of x and y values.
    Returns slope and y intercept of the line.
    """
    assert len(x) == len(y), f"len(x) != len(y) in Deming regression function"
    n = len(x)
    # get means of x and y
    x_bar = 0
    y_bar = 0
    for i in range(n):
        x_bar += x[i]
        y_bar += y[i]
    x_bar = x_bar / n
    y_bar = y_bar / n
    # get sxx, syy and sxy terms, using accumulator
    sxx = 0
    syy = 0
    sxy = 0
    for i in range(n):
        sxx += (x[i] - x_bar) ** 2
        syy += (y[i] - y_bar) ** 2
        sxy += (x[i] - x_bar) * (y[i] - y_bar)
    sxx *= (1 / (n - 1))
    syy *= (1 / (n - 1))
    sxy *= (1 / (n - 1))
    # compute m with equation
    m = (syy - sxx + math.sqrt((syy - sxx) ** 2 + 4 * sxy ** 2)) / (2 * sxy)
    # compute b with equation
    b = y_bar - m * x_bar
    return m, b

def main():
    x = [5, 3, 8]
    y = [4, 2, 3]
    result = linear_regression_deming(x, y)
    print(result)

if __name__ == '__main__':
    main()
