"""Modify to only print number for every 10th line"""

##def line_numbers(file_name):
##    """Print the contents of the file with the given name with each line
##    preceded by a line number.
##
##    Args:
##        file_name (str): Name of a .txt file
##
##    Returns:
##        None
##    """
##
##    text_file = open(file_name, 'r', encoding = 'utf-8')
##    line_count = 1
##    for line in text_file:
##        print('{0:<5} {1}'.format(line_count, line[:-1]))
##        line_count = line_count + 1
##    text_file.close()

def line_numbers_file(file_name, new_file_name):
    """Write the contents of the file file_name to the file new_file_name, with
    each line preceded by a line number.

    Args:
        file_name (str): Name of a .txt file
        new_file_name (str): Name of output .txt file.

    Returns:
        None
    """
    
    text_file = open(file_name, 'r', encoding = 'utf-8')
    new_text_file = open(new_file_name, 'w', encoding = 'utf-8')
    line_count = 1
    for line in text_file:
        if line_count % 10 == 0:
            new_text_file.write('{0:<5} {1}\n'.format(line_count, line[:-1]))
        else:
            new_text_file.write('      {}\n'.format(line[:-1]))
        line_count = line_count + 1
    text_file.close()
    new_text_file.close()

def sol_man(file_name):
    text_file = open(file_name, 'r', encoding = 'utf-8')
    line_count = 1
    for line in text_file:
        if (line_count - 1) % 10 == 0:
            print('{0:<5} {1}'.format(line_count, line[:-1]))
        else:
            print('      ' + line[:-1])
        line_count = line_count + 1
    text_file.close()

fname = '2701_0.txt'
##line_numbers(fname)
##line_numbers_file(fname, 'moby_dick_line_numbered.txt')
sol_man(fname)
