from matplotlib import pyplot
import _5_linear_regression_deming as e5

def linear_regression(x, y):
    """Returns the slope and y-intercept of the least squares regression
    line for the points whose x and y coordinates are stored in the lists
    x and y).

    Only use one loop.
    """
    assert len(x) == len(y), "x and y lists not same length"
    n = len(x)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_sqr = 0
    for i in range(len(x)):
        sum_x += x[i]
        sum_y += y[i]
        sum_xy += x[i] * y[i]
        sum_x_sqr += x[i] ** 2
    # compute slope
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sqr - (sum_x ** 2))
    intercept = (sum_y - slope * sum_x) / n
    return (slope, intercept)

def plot_regression(x, y, x_label, y_label, deming=False):
    # In-chapter example transcribed here for expediency.
    """
    Plot points in x and y with a linear regression line.

    Args:
        x (list): List of x values (independent variable)
        y (list): List of y values (dependent variable
        x_label (str): A string to label the x axis
        y_label (str): A string to label the y axis
        deming (bool): True if Deming linear regerssion method should be used

    Returns:
        None
    """
    pyplot.scatter(x, y)
    if deming ==  True:
        m, b = e5.linear_regression_deming(x, y)
    else:
        m, b = linear_regression(x, y)
    min_x = min(x)
    max_x = max(x)
    pyplot.plot([min_x, max_x], [m * min_x + b, m * max_x + b], color = 'red')
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.show()

def get_hw_exam_data():
    """Returns x list and y list for the exercise 8.6.2 data."""
    hw_scores = [63, 91, 81, 67, 100, 87, 91, 74, 26, 100, 78, 59, 85, 69]
    exam_scores = [73, 99, 98, 82, 97, 99, 96, 77, 33, 98, 100, 81, 38, 74]
    assert len(hw_scores) == len(exam_scores), f"hw_scores had {len(hw_scores)}, exam had {len(exam_scores)}" 
    return hw_scores, exam_scores

def main():    
    x = [5, 3, 8]
    y = [4, 2, 3]
    result = linear_regression(x, y)
    assert result == (3/19, 41/19), f"fail: {result}"
    print("ok")
##    plot_regression(x, y, 'x label', 'y label')
    hw_scores, exam_scores = get_hw_exam_data()
    plot_regression(hw_scores, exam_scores, 'homework score', 'exam score')
    plot_regression(hw_scores, exam_scores, '[deming regression] homework score', 'exam score', deming=True)

if __name__ == "__main__":
    main()
