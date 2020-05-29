def profit(prices):
    """Find the maximum achievable profit from a list of daily stock prices.

    Args:
        prices (list): a list of numbers

    Returns:
        (float): the maximum profit possible by buying on lowest day and selling
            on highest subsequent day.
    """
    # divide-conquer-combine
    if len(prices) <= 1: # Base case
        return 0

    mid_index = len(prices) // 2 # "divide" list in half
    left_profit = profit(prices[:mid_index]) # "conquer" each half
    right_profit = profit(prices[mid_index:])

    buy = min(prices[:mid_index])   # min price on the left
    # (any price in the left slice temporally precedes every price in the right)
    sell = max(prices[mid_index:]) # max price on the right
    mid_profit = sell - buy
    return max(left_profit, right_profit, mid_profit) # "combine" the three cases

prices = [3.90, 3.60, 3.65, 3.71, 3.78, 4.95, 3.21, 4.50, 3.18, 3.53]

actual = profit(prices)
print(actual)

