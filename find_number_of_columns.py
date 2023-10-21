from csv import reader
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f = open(data)
    f = reader(f)
    l = []
    for i in f:
        l.append(i[1])
    print(l[-1:])
print(find_number_of_columns("data.csv"))

# Read the csv file