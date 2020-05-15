import _1_linear_regression_and_plotreg as pr

def read_data(filename):
    """Reads data from the sat.csv file from the book's website and returns
    a tuple of two lists contining the data in the first and fourth columns
    of the file (high school GPAs and college GPAs)."""
    hs = []
    col = []
    file = open(filename, mode='r', encoding='utf-8')
    header = file.readline()
    for line in file:
        row = line.split(',')
        hs.append(float(row[0]))
        col.append(float(row[3]))
    file.close()
    return hs, col

def read_data_sat_college(filename):
    """Return tuple with sat score and college GPA. Combined math and verbal."""
    sat = []
    col = []
    file = open(filename, mode='r', encoding='utf-8')
    header = file.readline()
    for line in file:
        row = line.split(',')
        sat.append(float(row[1]) + float(row[2]))
        col.append(float(row[3]))
    file.close()
    return sat, col



filename = 'sat.csv'
hs, col = read_data(filename)
pr.plot_regression(hs, col, 'High School GPA', 'College GPA')
sat, col = read_data_sat_college(filename)
pr.plot_regression(sat, col, 'Combined sat math+verbal', 'college GPA')

    
