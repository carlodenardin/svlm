def extract_from_sorted(numbers: list[int], kint: int) -> int:
    """
    Start
    Input Data: a list of integers and a key integer kint
    Sorting: sort the list in ascending order
    Index Extraction: return the element at index [-kint] from the sorted list
    End
    """
    data = list(numbers)
    data.sort()
    return data[-kint]