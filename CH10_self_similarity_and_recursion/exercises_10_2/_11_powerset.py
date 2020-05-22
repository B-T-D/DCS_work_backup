def powerset(n):
    """Returns a list of all subsets of the integers 1, 2, ..., n. I.e. a set
    of all subsets (the "power set"). Subset meaning a list of zero or more
    unique items."""
    if n <= 1:
        return [[], [i for i in range(n, 0, -1)]]
    pset = powerset(n - 1)
    new_pset = pset.copy()
    for element in pset:
        new_element = element.copy()
        new_element.append(n)
        new_pset.append(new_element)
    pset = new_pset
    return pset

def subsets(n): # solman. Not renaming it here to avoid recursive calls confusion
    # Unclear if this is even the answer to the same problem. Some kind of typo in book, switches function
    #   names, gives example output for non-specified input "n" that I inferred meant n = 3.
    if n == 0:
        return [[]]
    without_n = subsets(n - 1) # he does pretty much same thing I did for the recursive-heart
    with_n = []
    for subset in without_n:
        with_n.append([n] + subset)
    return without_n + with_n

##print(powerset(1))
##print(f"-------attempt for n = 2:-------")
##print(f"\tRETURNED: {powerset(2)}")
##print(f"-------attempt for n = 3:-------")
##print(f"\tRETURNED: {powerset(3)}")
##print(f"----------for n = 4:-----------")
##print(f"\tRETURNED: {powerset(4)}")


n = 3
control = [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
returned = powerset(n)
print(returned)

for i in range(len(control)):
    for j in returned[i]:
        assert j in control[i], f"{j} not in {control[i]}"
print("\t\t----passed main set inclusion test----")


print("-----------comparison with book's:--------")
nvals = [1, 2, 3, 4]
print(f"{'n':10} | {'mine':30} | {'books':30}")
for n in nvals:
    print(f"{n:10} | {str(powerset(n)):30} | {str(subsets(n)):30}")
