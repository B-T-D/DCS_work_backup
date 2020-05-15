
def decode(word):
    """Decodes a string that was encoded using exercise 6.6 function."""
    decoded = ''
    end = ''
    # split it into even parts, with a single char end part if odd number chars
    even = word[0:(len(word) // 2)]
    if len(word) % 2 != 0:
        odd = word[(len(word) // 2 + 1):]
        end = word[len(word) // 2]
    else:
        odd = word[len(word) // 2:]    
    for i in range(len(word) // 2):
        decoded += even[i]
        decoded += odd[i]
    decoded += end
    return decoded

"""Book's was cleaner."""

def sol_man(word):
    mid = (len(word) + 1) // 2 # The midpoint of the word
    even = word[:mid]
    odd = word[mid:]
    decoded = ''
    for i in range(mid):
        decoded += even[i]
        if i < len(odd): # i will be less than len(odd) for every character up to the midpoint char in a word that has a midpoint (i.e. len(word) is odd).
            decoded += odd[i] # First character of odd will be the middle character if len(string) was odd.
    return decoded

print(decode('cmuesoptr'))
print(decode('peiurvos')) # 'previous' for even numbered
print('---')
print(sol_man('cmuesoptr'))
print(sol_man('peiurvos'))


        
