import matplotlib.pyplot as pyplot

def plot_profit(max_price):

    profits_list = []
    prices_list = []

    for price in range(1, 2 * max_price + 1):
        price = price / 2
        prices_list.append(price)
        sales = 2500 - 80 * price
        income = sales * price
        profit = income - 8000
        profits_list.append(profit)

    pyplot.plot(prices_list, profits_list)
    pyplot.xlabel('Ticket price')
    pyplot.ylabel('Profit')
    pyplot.show()

plot_profit(100)
