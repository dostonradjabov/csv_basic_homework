def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    from csv import reader
    f = open(data)
    f = reader(f)
    a = []
    for i in f:
        a.append(i[0])
    return i[:1]
print(get_first_column("data.csv"))    
# Read the csv file