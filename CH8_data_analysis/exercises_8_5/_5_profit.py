def profit(prices):
    """Returns a tuple containing the most profitable buy and sell days for the
    given list of prices."""
    best = (0, 1)

    for buy in range(len(prices) - 1):
        print(f"for buy price {prices[buy]} at index {buy}:")
        for sell in range(buy + 1, len(prices)):
            print(f"for sell price {prices[sell]} at index {sell}: ")
            if prices[sell] - prices[buy] > prices[best[1]] - prices[best[0]]:
                best = (buy, sell)
                print(f'\t**updated best to {best},\
profit would be {prices[best[1]] - prices[best[0]]} \
from buying at {prices[best[0]]} and selling at {prices[best[1]]}**')
        print('---')
    
##    for buy in prices:
##        for sell in prices[prices.index(buy):]: # Can only sell on days after the buy date
##            if sell - buy > best[1] - best[0]:
##                best = (buy, sell)
    return best

prices = [3, 2, 1, 5, 3, 9, 2]
correct_tuple = (2, 5)

days = profit(prices)
assert days == correct_tuple, f"returned {days}"

# test that doesn't just return the max and min price days regardless of
#   which day happens first
prices = [100, 5, 3, 1, 5, 10]
correct_tuple = (3, 5)
days = profit(prices)
assert days == correct_tuple, f"returned {days}"

print('ok')
