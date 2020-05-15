import turtle

def profit_plot(tortoise, max_price):
    """ """
    # To prevent tortoise drawing nonsensical downward line from origin to
    #   first plotted point:
    tortoise.up() # Raise the tortoise drawing pen
    tortoise.goto(0, -15000) # Move it manually to the lowest x, y pair on the
        # world coordinates we set in main().
    tortoise.down() # Put the drawing pen back down. 
    for price in range(1, 2* max_price + 1):
        price = price / 2
        sales = 2500 - 80 * price
        income = sales * price
        profit = income - 8000
        tortoise.goto(price, profit)
        

def main():
    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setworldcoordinates(0, -15000, 25, 15000)
    profit_plot(george, 25)
    screen.exitonclick()

main()
