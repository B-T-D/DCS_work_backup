#!/usr/bin/env python3

def linearRegression(x, y):
    pass

def plotRegression(x, y, xLabel, yLabel):
    """Plot points in x and y with a linear regression line.

    Parameters:
        x: a list of x values (independent variable)
        y: a list of y values (dependent variable)
        xLabel: a string to label the x axis
        yLabel: a string to label the y axis

    Return value: None
    """

    pyplot.scatter(x, y)
    m, b = linearRegression(x, y)
    minX = min(x)
    maxX = max(x)
    pyplot.plot([minX, maxX], [m * minX + b, m * maxX + b], color = 'red')
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.show()
