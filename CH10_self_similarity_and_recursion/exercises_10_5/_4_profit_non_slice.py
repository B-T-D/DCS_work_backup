



def profit(prices, first, last):
    """Find the maximum achievable profit from a list of daily stock prices.

    Args:
        prices (list): a list of numbers

    Returns:
        (float): the maximum profit possible by buying on lowest day and selling
            on highest subsequent day.
    """
    if last <= first: # because then the len is <= 1
        return 0
##    if len(prices[first:last]) <= 1:
##        return 0
##    if len(prices[first:last]) == 2:
##        return(max(prices[first:last]))
    mid_index = (first + last) // 2
    left_profit = profit(prices, first, mid_index)
    right_profit = profit(prices, mid_index + 1, last)
    buy = min(prices[:mid_index + 1])
    sell = max(prices[mid_index + 1:last + 1])
    mid_profit = sell - buy
    return max(left_profit, right_profit, mid_profit)

prices = [3.90, 3.60, 3.65, 3.71, 3.78, 4.95, 3.21, 4.50, 3.18, 3.53]

first = 0
last = len(prices) - 1
actual = profit(prices, first, last)
print(actual)
