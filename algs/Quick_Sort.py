
def sort(data):
    """
    The sort function sorts the given dataset by using the Quick Sort algorithm.\n
    **-- Time Complexity --**
    \n
    Best Case: O(n log(n))\n
    Worst Case: O(n^2)\n
    **-- Space Complexity --**
    \n
    O(log(n))\n
    :param data: A list of alphanumerical values
    """

    if len(data) <= 1:
        return data
    less_than_pivot = []
    greater_than_pivot = []
    pivot = data[0]
    for value in data[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return sort(less_than_pivot) + [pivot] + sort(greater_than_pivot)
