def profit(prices, first, last):
    """Returns the most profitable buy and sell days instead of the maximum
    profit.

    Args:
        prices (list): a list of numbers
        first (int): index position of the first day to consider buying/selling
            on.
    """
    if last <= first:
        return (first, first)
    mid_index = (first + last) // 2
    (left_buy, left_sell) = profit(prices, first, mid_index)
    (right_buy, right_sell) = profit(prices, mid_index + 1, last)

    buy = mid_index
    for index in range(first, mid_index):
        if prices[index] < prices[buy]:
            buy = index

    sell = mid_index + 1
    for index in range(mid_index + 2, last + 1):
        if prices[index] > prices[sell]:
            sell = index

    if prices[left_sell] - prices[left_buy] >=\
       max(prices[right_sell] - prices[right_buy], prices[sell] - prices[buy]):
        return left_buy, left_sell
    if prices [right_sell] - prices[right_buy] >= prices[sell] - prices[buy]:
        return right_buy, right_sell
    return buy, sell
    

prices = [3.90, 3.60, 3.65, 3.71, 3.78, 4.95, 3.21, 4.50, 3.18, 3.53]

first = 0
last = len(prices) - 1

actual = profit(prices, first, last)
expected = 1, 5 # max profit is 1.35, buying at 3.6 on [1] and selling at 4.95 on [5]
assert actual == expected, f"actual {actual}, expected {expected}"
print(f"passed quick test")
