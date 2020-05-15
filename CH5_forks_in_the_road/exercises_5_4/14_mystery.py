# Book's was different...moderately cleaner i think. 

def mystery(a, b):
    """..."""
    length = 2
    original_a = a
    original_b = b
    new_a = 'a'
    new_b = 'b'
    while True:
        new_b = get_next_term(a, b)
        new_a = b
        length += 1
        a = new_a
        b = new_b
        if a == original_a and b == original_b:
            return length

def get_next_term(a, b):
    return (a + b) % 10
        
        

a = 1
b = 1
##print(confirm_sequence(17, a, b))
print(mystery(a, b))

