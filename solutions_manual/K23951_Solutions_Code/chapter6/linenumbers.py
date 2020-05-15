#!/usr/bin/env python3
    
def lineNumbers(fileName):
    """Print the contents of the file with the given name 
       with each line preceded by a line number.
    
    Parameter:
        fileName: the name of a text file
        
    Return value: None
    """
    
    textFile = open(fileName, 'r', encoding = 'utf-8')
    lineCount = 1
    for line in textFile:
        print('{0:<5} {1}'.format(lineCount, line[:-1]))
        lineCount = lineCount + 1
    textFile.close()

def lineNumbersFile(fileName, newFileName):
    """Write the contents of the file fileName to the file
       newFileName, with each line preceded by a line number.
    
    Parameters:
        fileName: the name of a text file
        newFileName: the name of the output text file
        
    Return value: None
    """

    
    textFile = open(fileName, 'r', encoding = 'utf-8')
    newTextFile = open(newFileName, 'w')
    lineCount = 1
    for line in textFile:
        newTextFile.write('{0:<5} {1}\n}'.format(lineCount, line[:-1]))
        lineCount = lineCount + 1
    textFile.close()
    newTextFile.close()
    
