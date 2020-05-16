"""Calls the readdata function for the Wisconsin min-max temps data,
and then repeatedly asks for a date string to search for in the table and
outputs the correxpnding min temp."""

def read_data():
    """(Copied from book 444)
    Read monthly extreme temperature data into a table.

    Args:
        None

    Returns:
        (list): A list of lists containing monthly extreme temperature data.
    """
    data_file = open('madison_temp.csv', 'r')
    header = data_file.readline()
    table = {}
    for line in data_file:
        row = line.split(',')
        row[3] = int(row[3])
        row[4] = int(row[4])
        table[row[2]] = [row[3], row[4]]
    data_file.close()
    return table

def get_min_temp(table, date):
    """Return the minimum temperature for the month with the given date string.

    Args:
        table (list): A list storing a table of the extreme temp data
        date (str): A date string in format YYYYMMDD

    Returns:
        (int): Minimum temperature for the date or None if date doesn't exist
    """
    if date in table:
        return table[date][1]
    return None

def get_max_temp(table, date):
    """returns the max temp instead of the min"""
    num_rows = len(table)
    for r in range(num_rows):
        if table[r][0] == date:
            return table[r][1]

def main():
    data = read_data()
    date = ''
    date = input("Enter a date in format YYYYMMDD: ")
    while date != 'quit':
        result = get_min_temp(data, date)
        print(result)
        date = input("Enter a date in format YYYYMMDD: ")

if __name__ == '__main__':
    main()
