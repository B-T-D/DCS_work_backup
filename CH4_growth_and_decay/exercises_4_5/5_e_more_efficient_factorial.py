def e(n):
    """
    Approximates the value of Euler's number e by computing n finite number of
    iterations of 1 + (1/i!).
    
    Args:
        n (int): Number of terms to add, i.e. iterations to use in the approximation.

    Returns:
        (float): Approximate value of e for n iterations. 
    """
    sum = 1
    factorial = 1
    for i in range(1, n):
        factorial = factorial * i
        sum = sum + 1 / factorial # Using 1.0 here as book does, caused OverFlowError int
            # too large to convert to float at n = 1000.
    return sum
    

print(e(4))
print(e(1000))
