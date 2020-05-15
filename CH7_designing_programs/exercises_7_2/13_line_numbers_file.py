import os

def line_numbers(filename):
    """
    Precondition:
        filename is a string containing the name of a .txt file with bytes
        encoded using utf-8 and accessible by the python interpreter

    Postcondition:
        Prints each line of the file with a line number at the start of the
        line. 

    """
    assert isinstance(filename, str), 'file name must be a string'
    assert os.path.isfile(filename), 'file by that name not accessible'
    assert os.access(filename, os.R_OK), 'file not readable'
    textfile = open(filename, 'r', encoding='utf-8')
    line_count = 1
    for line in textfile:
        print('{0:<5} {1}'.format(line_count, line[:-1]))
        line_count += 1
    textfile.close

line_numbers({'is this a dict': 'yes'})
line_numbers('poot.txt')
line_numbers(r"C:\Users\Ben\Desktop\Python_DCS_book\CH7_designing_programs\2701_0.txt")

