def encode(word):
    """Returns a string encoded by rearranging to have all even indexed chars
    followed by all odd-indexed chars."""

    # make a substring of the even index characters
    first_half = ''
    for i in range(0, len(word), 2):
        first_half += word[i]
    # make second substring of odd chars
    second_half = ''
    for i in range(1, len(word), 2):
        second_half += word[i]
    return first_half + second_half

"""Book's is more elegant."""

def sol_man(word):
    even = ''
    odd = ''
    for i in range(len(word)):
        if i % 2 == 0:
            even += word[i]
        else:
            odd += word[i]
    return even + odd
    

print(encode('computers'))
print(sol_man('computers'))
print(encode('previous'))
