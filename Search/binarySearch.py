def binarySearch(array, element, size):
    begin = 0
    end = size - 1
    middle = 0

    while begin <= end:
        middle = int((begin + end) / 2)
        if array[middle] < element:
            begin = middle + 1
        elif array[middle] > element:
            end = middle - 1
        else:
            return middle

    return -1
