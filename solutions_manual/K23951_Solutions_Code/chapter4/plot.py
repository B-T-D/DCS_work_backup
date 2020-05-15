#!/usr/bin/env python3

import turtle

def profitTable(maxPrice):
    """Prints a table of profits from a show based on ticket price.
    
    Parameters:
        maxPrice: maximum price to consider
        
    Return value: None
    """
    
    print('Price     Income      Profit')
    print('------   ---------   ---------')
    for price in range(1, maxPrice + 1):
        sales = 2500 - 80 * price
        income = sales * price
        profit = income - 8000
        formatString = '${0:>5.2f}  ${1:>8.2f}  ${2:8.2f}'
        print(formatString.format(price, income, profit))
        

def profitPlot(tortoise, maxPrice):
    """Plots profit from a show based on ticket price.
    
    Parameters:
        tortoise: a Turtle object
        maxPrice: maximum price to consider
        
    Return value: None
    """
    
    for price in range(1, 2 * maxPrice + 1):
        realPrice = price / 2
        sales = 2500 - 80 * realPrice
        income = sales * realPrice
        profit = income - 8000
        tortoise.goto(realPrice, profit)
        
def main():
    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setworldcoordinates(0, -15000, 25, 15000)
    profitPlot(george, 25)
    screen.exitonclick()
    
main()
