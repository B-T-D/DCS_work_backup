from _5_swap import swap

def reverse(data):
    """Reverses the list data in place

    Returns:
        None
    """
    start = 0
    end = len(data) - 1
    while start < end:
        swap(data, start, end)
        start += 1
        end -= 1

def sol_man(data):
    for index in range(len(data) // 2):
        swap(data, index, -(index + 1) # negates index to start from the end of the list
             

data = ["Linda", "monster,", "a", "You're"]
reverse(data)
print(data)

string = "above. did we as version, comprehension list the and version loop \
original the of parts corresponding the at carefully Look"
data_2 = string.split() #make it into a list of its words
print(data_2)

data_3 = ["What", "happens", "with", "odd", "number", "of", "words?"]
temp_data_3 = data_3.copy()
reverse(data_3)
reverse(data_3)

assert data_3 == temp_data_3, f"fail {data_3}"

correct_string = "Look carefully at the corresponding parts of the original loop \
version and the list comprehension version, as we did above."
correct_list = correct_string.split()

reverse(data_2)
assert data_2 == correct_list, f"fail {data_2}"



    
