
# Tale of two cities:
##    http://www.gutenberg.org/files/98/98-0.txt

import sys

sys.path.append(
    'C:\\Users\\Ben\\Desktop\\Python_DCS_book\\CH6_text_documents_and_dna'
    )

import c1_word_count as wc
import urllib.request as web

def wc_web(url):
    """Reads a text file from the web at the given URL and returns the number
    of words in the file using the final wordcount_5 function from 6.1
    chapter-body."""
    text = get_text(url)
    return wc.word_count_5(text)
    

def get_text(url):
    """Returns the contents of a url txt file as a string."""
    webpage = web.urlopen(url)
    text = webpage.read()
    webpage.close()
    text = text.decode('utf-8')
    return text

def sol_man(url):
    text_file = web.urlopen(url)
    text = text_file.read()
    text = text.decode('utf-8')
    text_file.close()
    return wc.word_count_5(text)
    

url = 'http://www.gutenberg.org/files/98/98-0.txt'
print(wc_web(url))
##print(get_text(url))
print(f"Book's: {sol_man(url)}")
