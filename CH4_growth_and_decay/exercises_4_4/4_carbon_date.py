def carbon_date(original_amount, fraction_remaining, dt):
    amount = original_amount
    k = -0.00012096809434
    iterations = 0
    while amount > original_amount * fraction_remaining:
        amount = amount + k * amount * dt
        iterations += 1
    return iterations * dt

print(carbon_date(100, 0.7, 0.001))
