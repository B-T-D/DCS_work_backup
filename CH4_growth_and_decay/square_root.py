import math

def sqrt(n, k):
    """
    Approximates the square root of n with k iterations of the Babylonian
    method.

    Args:
        n (int): The number to take the square root of
        k: Number of iterations

    Returns:
        (float): Approximate square root of n
    """

    x = 1.0
    for index in range(k):
        x = 0.5 * (x + n / x)
    return x

def match_math_sqrt(n):
    """
    Returns the number of iterations of the sqrt(n, k) function needed to
    match the value returned by the math module's sqrt function.
    """
    k = 1
    while sqrt(n, k) != math.sqrt(n):
        print("-----")
        print(f"k is {k}")
        print(f"DIY sqrt is {sqrt(n, k)}")
        k += 1
    return k

    # Appears to loop infinitely due to some limiter on the number of decimal
    #   places of the return from the DIY sqrt function. Moving on bc not
    #   a major focus for the book. Could see how you could use an ML style loss
    #   function to adjust k more efficiently than just incrementing by 1 (because
    #   you have a known value of math.sqrt(n) to check against to tell you how
    #   far off). 

n = 10
for i in range(100):
    print(f"{i} iterations | {sqrt(n, i)}")

##i = int(1e3)
##print(f"{i} iterations | {sqrt(n, i)}")
##
##i = int(1e5)
##print(f"{i} iterations | {sqrt(n, i)}")
##
##i = int(1e6)
##print(f"{i} iterations | {sqrt(n, i)}")
##
##print("------")

print(f"math.sqrt(10) returns: {math.sqrt(10)}")

print(match_math_sqrt(10))
