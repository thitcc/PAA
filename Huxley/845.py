def binarySearch(array, element, size):
    begin = 0
    middle = 0
    end = size - 1

    while begin <= end:
        middle = int((begin + end) / 2)
        if array[middle] < element:
            begin = middle + 1
        elif array[middle] > element:
            end = middle - 1
        else:
            return middle


trees, woods = input().split()

treeHeight = []

for i in input().split():
    treeHeight.append(int(i))

treeHeight.sort()


