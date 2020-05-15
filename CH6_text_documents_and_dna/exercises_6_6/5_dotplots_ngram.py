import matplotlib.pyplot as pyplot

def dotplot(text1, text2, n):
    """Generalize the dotplot function so that it compares n-grams instead of
    individual characters.

    Args:
        text1 (str): A string object of length x
        text2 (str): A string object also of length x
        n (int): Length of substring to compare. 

    Returns:
        None
    """

    text1 = text1.lower()
    text2 = text2.lower()
    x = []
    y = []
    for index in range(len(text1) - n + 1):
        for index2 in range(len(text2) - n + 1):
            if text1[index:index + n] == text2[index2:index2 + n]:
                x.append(index)
                y.append(index2)
    

    # Pyplot calls
    pyplot.scatter(x, y) # scatter plot
    pyplot.xlim(0, len(text1)) # x axis covers entire text1
    pyplot.ylim(0, len(text2)) # y axis covers entire text2
    pyplot.xlabel(text1)
    pyplot.ylabel(text2)
    pyplot.show()

text1 = "Peter Piper picked a peck of pickled peppers."
text2 = "Peter Pepper picked a peck of pickled capers."
dotplot(text1, text2, 1)
dotplot('reaeraewsuoi', 'iumknlkuynkounreyopmb', 1)
