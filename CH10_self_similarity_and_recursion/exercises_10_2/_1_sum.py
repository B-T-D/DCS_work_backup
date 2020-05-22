def sum(n):
    """Returns the sum of integers from 1 to n, using recursion."""
    # base case is adding up [1..1], i.e. just 1
    if n <= 1: # only works on positive integers (this is how solman's is)
        return 1
    # recursive case:
    return n + sum(n - 1)

n = 5
checksum = 1 + 2 + 3 + 4 + 5

returned_sum = sum(n)

assert returned_sum == checksum, f"returned {returned_sum}"
print(returned_sum)

print(sum(-1))
