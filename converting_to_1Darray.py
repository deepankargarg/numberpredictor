
def to_1D_array(data):
    """
    Converts a 2D array to a 1D array.

    Parameters:
    data (list of list): The input 2D array.

    Returns:
    list: The converted 1D array.
    """
    return [(item/255) for sublist in data for item in sublist]