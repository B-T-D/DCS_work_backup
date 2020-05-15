def profit_table(max_price):
    """Prints a table of profits from a show based on ticket price.

    Args:
        max_price: Maximum price to consider

    Returns:
        None
    """

    print('Price    Income    Profit')
    print('-----    ------    -------')
    for price in range(1, 2 * max_price + 1):
        price = price / 2
        sales = 2500 - 80 * price
        income = sales * price
        profit = income - 8000
        format_string = '${0:>5.2f} ${1:>8.2f} ${2:8.2f}'
        print(format_string.format(price, income, profit))

def main():
    profit_table(25)

main()
