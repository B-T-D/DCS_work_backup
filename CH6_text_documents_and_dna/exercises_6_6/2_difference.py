
def difference(word1, word2):
    """Return the first index at which the strings differ. If the words have
    different lengths, and shorter word is a prefis of the longer, return
    len(shorter_word). Return -1 if words are identical.

    Without directly testing whether word1 and word2 are equal."""

    for index1 in range(len(word1)):
        if word1[index1] != word2[index1]:
            return index1
        elif index1 > len(word2) - 1:
            return len(word2)
    return -1

def sol_man(word1, word2):
    index = 0
    while index < len(word1) and index < len(word2) and word1[index] == word2[index]:
        index = index + 1
    if len(word1) == len(word2) and index == len(word1):
        return -1
    return index


        
##        for index2 in range(len(word2)):
##            print("word1[index1] == word2[index2]?")
##            print(f"{word1[index1]} == {word2[index2]}?")
##            print(word1[index1] == word2[index2])
##            if word1[index1] != word2[index2]:
##                return index2

##print(difference('spam', 'spxx'))
##print(difference('spam', 'spam'))
##print(difference('spam', 'spa'))
##print(difference('spa', 'spam'))

print(sol_man('spam', 'spxx'))
print(sol_man('spam', 'spam'))
print(sol_man('spam', 'spa'))
print(sol_man('spa', 'spam'))
