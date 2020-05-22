

def palindrome_iter(s):
    """Iterative function to determine whether a string is a palindrome.
    Returns (bool) True if s is a palindrome else False
    """
    for index in range(len(s) // 2):
        if s[index] != s[-(index + 1)]:
            return False
    return True

def palindrome_recursive(s):
    if len(s) <= 1: # base case, empty or single-char string is always palindrome
        return True
    return s[0] == s[-1] and palindrome_recursive(s[1:-1])
        # ^^ Second base case built in here (?), i.e. comparing first and
        #   last characters before the recursive call


strings = ['radar', 'spam', 'now i won', 'star rats', 'palindrome']

for s in strings:
    print(f"string: {s}")
    print(f"palindrome: {palindrome_iter(s)}")
    print('----')

print("--Recursive--")
for s in strings:
    print(f"string: {s}")
    print(f"palindrome: {palindrome_recursive(s)}")
    print('----')
    
