#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    from csv import reader
    f = open(data)
    f = reader(f)
    a = []
    for i in f:
        a.append(i[1])
    return a[1:]
print(get_column_names("data.csv"))
# Read the csv file