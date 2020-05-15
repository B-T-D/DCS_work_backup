def halflife_c14(original_amount, dt):
    k = -0.000121 # Decay constant for carbon 14
    amount = original_amount
    years = 0 # Mine was fine, just not conceptually right to call this "years"
    while amount > original_amount / 2:
        amount = amount + k * amount * dt    
        years += 1
    return years * dt # Actual conceptual "years" are the number of iterations multiplied by the fractional iterations per year (IOW divided by iterations per year, dt=0.01 would be 100 iterations in a year).


def sol_man(original_amount, dt):
    amount = original_amount
    k = -0.000121
    iterations = 0
    while amount > original_amount / 2:
        amount = amount + k * amount * dt
        iterations = iterations + 1
    return iterations * dt

print(halflife_c14(100, 1))
print(sol_man(100, 1))
        
        
        
