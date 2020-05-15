import matplotlib.pyplot as pyplot

def word_frequency(filename, word, windowsize, skip):
    """
    """
    textfile = open(filename, 'r', encoding='utf-8')
    text = textfile.read() # One long string with the entire file contents
    textfile.close()
    count = 0
    start = 0
    x = []
    y = []
    for i in range(len(text)):
        window = text[start:start + windowsize]
        x.append(start)
        y.append(window.count(word))
        count += window.count(word)
        start += skip
    

    # pyplot calls
    pyplot.scatter(x, y)
    pyplot.xlabel("Window start location")
    pyplot.ylabel("Count in that window")
    pyplot.show()

def sol_man(filename, word, windowsize, skip):
    textfile = open(filename, 'r', encoding='utf-8')
    text = textfile.read() # One long string with the entire file contents
    textfile.close()

    freqs = []
    indices = range(0, len(text), skip)
    for index in indices:
        freqs.append(text[index:index + windowsize].count(word))

    # pyplot calls
    pyplot.scatter(indices, freqs, marker = '.')
    pyplot.xlabel('Location')
    pyplot.ylabel('Count')
    pyplot.xlim(0, len(text))
    pyplot.ylim(0, max(freqs))
    pyplot.show()
    


##moby_dick = r"C:\Users\Ben\Desktop\Python_DCS_book\CH6_text_documents_and_dna\2701_0.txt"
##word_frequency(moby_dick, 'whale', windowsize=10, skip=5)
word_frequency('test.txt', 'pe', windowsize=12, skip=2)
sol_man('test.txt', 'pe', windowsize=12, skip=2)
