
def interest(amount, rate, target):

    years = 0
    while amount < target:
        amount = (1 + rate) * amount
        years += 1
    return years

print(interest(1000, 0.03, 1200))
