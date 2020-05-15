import sys

sys.path.append(
    'C:\\Users\\Ben\\Desktop\\Python_DCS_book\\CH6_text_documents_and_dna'
    )

from c1_word_count import word_count_5 as wc

def wc_lines(filename):
    """Uses wc5 function to print the number of words in each line of the file
    with the given file name."""
    fobj = open(filename, 'r', encoding = 'utf-8')
    for line in fobj:
        print(wc(line))
    fobj.close()




fname = '2701_0.txt'

wc_lines(fname)
