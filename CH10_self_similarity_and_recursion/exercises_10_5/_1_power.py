def power(a, n):
    """Returns the value of a ** n, utilizing the fact that
    a ** n = (a ** (n/2)) ** 2  when n is even and
    ((a ** ((n - 1)/2)) ** 2) * a when n is odd.

    Args:
        n (int): non-negative integer.
    """
    if n == 0: # base case
        return 1
    if n == 2:
        return a * a
    if n % 2 == 0: # even recursive case
        return power(power(a, (n / 2)), 2)
    else:
        return power(power(a, (n - 1) / 2), 2) * a
    pass

# Mine seems "better" than solman in that I didn't resort to using the **
#   operator anywhere in the function, but that wasn't strictly disallowed.

def sm_power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return sm_power(a, n // 2) ** 2 # Why floor division?
    else:       # Floor division because it accomplishes the same thing as n-1.
                    # Does nothing for values that were already even, and for
                    # odd values is same as subtracting 1 then dividing by 2.
        return a * sm_power(a, n // 2) ** 2



test_cases = [(2, 6, 64),
              (2, 5, 32)]
for case in test_cases:
    a = case[0]
    n = case[1]
    expected = case[2]
    actual = power(a, n)
    assert actual == expected, f"actual {actual}, expected {expected}"
    actual = sm_power(a, n)
    assert actual == expected, f"actual {actual}, expected {expected}"




print(f"passed test_cases")
