def equal(list1, list2):
    """Recursive function that returns Boolean indicating whether the two lists
    are equal without testing whether list1 == list2. May only compare lenghts
    of the two lists, and test equality of individual list elements."""
    if len(list1) + len(list2) == 0: # solman caught me on this, i missed it. For handling empty lists
        return True
    if len(list1) != len(list2) or list1[0] != list2[0]:
        return False
    return equal(list1[1:], list2[1:])


def simple_case_lists_equal():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    assert equal(list1, list2) == True
    print("Equal lists test ok\n---")

def simple_case_lists_different():
    list1 = [1, 4, 5, 6, 3]
    list2 = [4, 5, 7, 3, 2]
    assert equal(list1, list2) == False
    print("Differing lists test ok\n---")

def same_values_different_order():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 5, 2, 4, 3]
    assert equal(list1, list2) == False
    print("Same elements different order test ok\n---")

def different_list_lengths():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8]
    assert equal(list1, list2) == False
    print("Different list lengths test ok\n---")

def empty_lists():
    """both lists empty"""
    list1 = []
    list2 = []
    assert equal(list1, list2) == True
    print("Both lists empty test ok\n---")

def test():

    simple_case_lists_equal()
    simple_case_lists_different()
    same_values_different_order()
    different_list_lengths()
    empty_lists()

test()
