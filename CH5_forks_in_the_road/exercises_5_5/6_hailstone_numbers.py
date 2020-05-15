
def hailstone(start):

    integers = []
    current = start
    while current != 1 or integers == []:
        if current % 2 == 0:
            next = current / 2
        else:
            next = current * 3 + 1
        integers.append(int(current))
        current = next
    integers.append(int(next)) # add the final number after exiting the loop
    print(integers)
    return len(integers)

# book didn't actually care about knowing the sequence, just returning the
#   number of integers in it. 

hailstone(3)

##
##numbers = [0, 1, 2, 3, 4, 5, 6]
##for i in numbers:
##    print(hailstone(i))
