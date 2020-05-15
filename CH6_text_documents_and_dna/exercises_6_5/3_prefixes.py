
def prefixes(word):
    """Prints all the 'prefixes' of the given word, meaning every substring
    from word[0] to the full word, word[0:len(word)]"""

    for index in range(1, len(word) + 1):
        print(word[0:index])
        # book is better:
##            word[:index], don't need zero at the start

def sol_man(word):
    for index in range(len(word)):
        print(word[:index])
    # This doesn't print the final full-string 'cart' though like the in-text
    # example says the function should. 

prefixes('cart')
sol_man('cart')
        
