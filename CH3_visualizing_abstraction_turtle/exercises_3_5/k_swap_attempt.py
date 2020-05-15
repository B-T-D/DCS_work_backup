"""
Ex 3.5.11
2020-03-28 20:59
"""


def swap(a, b):
    temp_a = a
    temp_b = b
    a = temp_b
    b = temp_a
##    return a, b


x = 10
y = 1
print(f"x is {x} and y is {y}")
x, y = swap(x, y)
print(f"x is {x} and y is {y}")
x = 10
y = 1
print(f"x is {x} and y is {y}")
##x, y = swap(x, y)
x, y = 2, 3

print(f"x is {x} and y is {y}")


class Swappers:

    def swap(self, a, b):
        temp_a = self.a
        temp_b = self.b
        self.a = temp_b
        self.b = temp_a


"""
This can't be done when the function doesn't return anything. It could be done
with a multiple assignment statement if the function returned the new values of
the inputs. It could also maybe be done, without returning anything,
with a class method for a class of which
x and y were instance objects.
"""
