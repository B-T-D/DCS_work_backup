#!/usr/bin/env python3

def readData():
    """Read monthly extreme temperature data into a table.
    
    Parameters: none
    
    Return value: a list of lists containing monthly extreme temperature data
    """

    dataFile = open('madison_temp.csv', 'r')
    header = dataFile.readline()
    table = []
    for line in dataFile:
        row = line.split(',')
        row[3] = int(row[3])
        row[4] = int(row[4])
        table.append(row[2:])  # add a new row to the table
    dataFile.close()
    return table
    
def getMinTemp(table, date):
    """Return the minimum temperature for the month 
       with the given date string.

    Parameters:
        table: a table containing extreme temperature data
        date: a date string

    Return value: 
        the minimum temperature for the given date 
        or None if the date does not exist
    """

    numRows = len(table)
    for r in range(numRows):
        if table[r][0] == date:
            return table[r][2]
    return None
