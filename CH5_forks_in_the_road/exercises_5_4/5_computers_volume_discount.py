

def cost(quantity):
    """Return cost of buying quantity computers from a distributor that gives
    a 5% discount for purchases of more than 20 machines. With base price $1500.
    """
    price = 1500
    if quantity <= 20:
        return quantity * price
    return quantity * price * 0.95

def cost_2(quantity, price, dth, discount):
    """
    Args:
        quantity (int):
        price (float):
        dth (int): The number of computers that must be purchased to get the
            volume discount.
        discount (float): Size of the volume discount expressed as decimal.
    """
    if quantity <= dth:
        return quantity * price
    return quantity * price * (1 - discount)
    
for i in range(0, 50):
    print(f"{i} | {cost(i)}")

price = 1500
dth = 10
discount = 0.07

for i in range(0, 50):
    print(f"{i} | {cost_2(i, price, dth, discount)}")
    


