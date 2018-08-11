def upper_bound(array, a):
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

    end = len(array) - 1 - index
    total = 0

    for index in range(end):
        total += array[index] - element

    if total == a:
        print('%.4f' % element)
    else:
        upper_bound(array)

    return index


n, a = [int(x) for x in input().split()]
while n != 0 and a != 0:
    height = [int(x) for x in input().split()]
    height.sort()
    total = sum(height)
    if total == a:
        print(":D")
    elif total < a:
        print("-.-")
    else:
        print('%.4f' % upper_bound(height, a))

    n, a = [int(x) for x in input().split()]
