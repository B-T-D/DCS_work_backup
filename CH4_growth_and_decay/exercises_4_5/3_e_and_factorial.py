def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return factorial

def e(n):
    """
    Args:
        n (int): Number of terms to add, i.e. iterations to use in the approximation.
    """
    sum = 1
    for i in range(1, n):
##        print(f"sum is {sum}")
        sum = sum + (1 / factorial(i))
##        print(f"after adding 1/{i}!, new sum is {sum}")
    return sum
    

print(factorial(5))
print(e(4))
print(e(1000))
