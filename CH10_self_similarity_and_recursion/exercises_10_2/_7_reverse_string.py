def reverse(text):
    """Returns the reverse of (str) text."""
    if len(text) <= 1:
        return text
    return text[-1] + reverse(text[1:-1]) + text[0]

def solman(text): # he puts each character onto the end one by one
        # rather than 'swapping' as I pictured it
    if text == '':
        return ''
    return solman(text[1:]) + text[0]
    


test_dict = {'text': 'txet',
             'reverse': 'esrever'}

for key in test_dict:
    text = key
    control = test_dict[key]
    returned = reverse(key)
    assert returned == control, f"{returned} != {control}"

words = ['recursive', 'function', 'now i won', 'converts', 'ass']

for word in words:
    print(reverse(word))

print('--sol man --')

for key in test_dict:
    text = key
    control = test_dict[key]
    returned = solman(key)
    assert returned == control, f"{returned} != {control}"
