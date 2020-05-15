#!/usr/bin/env python3

def profit(prices):
    """Find the maximum achievable profit from a list of daily 
       stock prices.

    Parameter:
        prices: a list of daily stock prices

    Return value: the maximum profit
    """

    if len(prices) <= 1:                        # base case
        return 0

    midIndex = len(prices) // 2                 # divide in half
    leftProfit = profit(prices[:midIndex])      # conquer 2 halves
    rightProfit = profit(prices[midIndex:])
    
    buy = min(prices[:midIndex])                # min price on left
    sell = max(prices[midIndex:])               # max price on right
    midProfit = sell - buy
    return max(leftProfit, rightProfit, midProfit) # combine 3 cases
    
def main():
    prices = [3.90, 3.60, 3.65, 3.71, 3.78, 4.95, 3.21, 4.50, 3.18, 3.53]
    myProfit = profit(prices)
    print(myProfit)
    
main()
