
def abc():
    """Prompts for a choice of A, B, or C and uses a while loop to keep
    prompting until it receives the string 'A', 'B', or 'C'."""
    string = ''
    while string != ('A' or 'B' or 'C'):
        string = input("Please enter one of 'A', 'B', or 'C': ")

abc()
        
