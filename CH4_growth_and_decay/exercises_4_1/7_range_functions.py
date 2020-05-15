
def sep():
    print('------')

# a
def print_even_ints():
    for i in range(2, 101, 2):
        print(i)

# b
def print_odd_ints():
    for i in range(1, 101, 2):
        print(i)

# c
def print_descending():
    for i in range(100, 0, -1):
        print(i)

# d
def subexercise_d():
    for i in range(7, 20, 4):
        print(i)

# e
def subexercise_e():
    for i in range(2, -3, -1):
        print(i)

def subexercise_f():
    for i in range(-7, -20, -4):
        print(i)

def main():
    print_even_ints()
    print('------')
    print_odd_ints()
    print('------')
    print_descending()
    print('------')
    subexercise_d()
    sep()
    subexercise_e()
    sep()
    subexercise_f()

main()
