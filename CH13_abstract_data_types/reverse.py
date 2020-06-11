import stack

def reverse(text):

    """Use the stack ADT to reverse a string."""

    character_stack = stack.Stack()
    for character in text:
        character_stack.push(character)

    reverse_text = ''
    while not character_stack.is_empty():
        character = character_stack.pop()
        reverse_text += character
    return reverse_text

text = 'test'
print(reverse(text))
