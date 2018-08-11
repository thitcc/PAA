def upper_bound(array):
    begin = 0
    end = len(array) - 1
    element = float((begin + end) / 2)
    index = -1

    while begin <= end:
        middle = int((begin + end) / 2)
        if array[middle] < element:
            begin = middle + 1
        elif array[middle] > element:
            end = middle - 1
            index = middle
        else:
            begin = middle + 1

    return index


n, a = [int(x) for x in input().split()]
while n != 0 and a != 0:
    height = [int(x) for x in input().split()]
    height.sort()
    print(upper_bound(height))
    n, a = [int(x) for x in input().split()]
