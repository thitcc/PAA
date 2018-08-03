def binarySearch(array, element, size):
    begin = 0
    end = size - 1

    while begin <= end:
        middle = int((begin + end) / 2)
        if array[middle] < element:
            begin = middle + 1
        elif array[middle] > element:
            end = middle - 1
        else:
            return middle

    return -1


def lower_bound(array, element):
    begin = 0
    end = len(array) - 1
    index = -1

    while begin <= end:
        middle = int((begin + end) / 2)
        if array[middle] < element:
            begin = middle + 1
        elif array[middle] > element:
            end = middle - 1
        else:
            end = middle - 1
            index = middle

    return index


def upper_bound(array, element):
    begin = 0
    end = len(array) - 1
    index = -1

    while begin <= end:
        middle = int((begin + end) / 2)
        if array[middle] < element:
            begin = middle + 1
        elif array[middle] > element:
            end = middle - 1
        else:
            begin = middle + 1
            index = middle

    return index
