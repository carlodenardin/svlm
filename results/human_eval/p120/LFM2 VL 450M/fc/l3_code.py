def process_data(data):
    """
    Processes the input data and returns the processed result.

    Args:
        data (list): The input data to be processed.

    Returns:
        list: The processed result.
    """
    result = []
    for item in data:
        if isinstance(item, list):
            result.append(process_data(item))
        elif isinstance(item, int):
            result.append(item)
        else:
            raise ValueError('Invalid data type. Only list and integer are allowed.')
    return result