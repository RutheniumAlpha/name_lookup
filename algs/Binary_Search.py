
def search(data, l, r, value):
    """
    The search function searches the given dataset for the value by using the Binary Search algorithm.\n
    **-- Time Complexity --**
    \n
    O(n)\n
    **-- Space Complexity --**
    \n
    O(1)
    :param data: A list of alphanumerical values
    :param value: The value to be searched
    :param l: Left
    :param r: Right
    """

    if r >= l:

        mid = l + (r - l) // 2

        if data[mid] == value:
            return mid

        elif data[mid] > value:
            return search(data, l, mid - 1, value)

        else:
            return search(data, mid + 1, r, value)

    else:
        return -1
