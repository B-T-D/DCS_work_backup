# quick code along only

def sol_man(filename):
    """Prints an alphabetized table of word frequencies in the text file
    with the given filename."""
    freq = {}
    input_file = open(filename, 'r', encoding= 'utf-8')
    for line in input_file:
        words = line.split()
        for word in words:
            word = word.strip('.!?,:;()\'"-')
            word = word.lower()
            if word in freq:
                freq[word] = freq[word] + 1
            else:
                freq[word] = 1
    input_file.close()
    words = list(freq.keys())
    words.sort()
    for word in words:
        print(word + ': ' + str(freq[word]))

filename = r"C:\Users\Ben\Desktop\Python_DCS_book\CH6_text_documents_and_dna\2701_0.txt"
sol_man(filename)
    
    
