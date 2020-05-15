def rsquared(x, y, m, b):
    """
    Args:
        x (list): List of x values
        y (list): List of y values
        m (float or fraction): Slope of the regression line for the set of points
        b (float or fraction): y-intercept of the regression line
    Returns:
        (float): The r-squared coefficient for the set of points.
    """
    assert len(x) == len(y), f"len(x) != len(y) in rsquared function"
    # get y-bar (mean y) for later use
    sum_y = 0
    for value in y:
        sum_y += value
    y_bar = sum_y / len(y)
    # iterate through the values to get the sums for the 'S' and 'T' terms:
    s = 0
    t = 0
    for i in range(len(x)):
        s += (y[i] - (m * x[i] + b)) ** 2
        t += (y[i] - y_bar) ** 2
    return 1 - s / t

x = [5, 3, 8]
y = [4, 2, 3]
m = 3/14
b = 13/7

assert round(rsquared(x, y, m, b), 10) == round(27/196, 10), f"fail on rsquared simple test values"
print("ok rsquared function")
