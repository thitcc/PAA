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

n, m = [int(x) for x in input().split()]
houses = [int(x) for x in input().split()]
delivery = [int(x) for x in input().split()]

time = 0
i = 0

for item in delivery:
    if item != houses[i]:
        position = binarySearch(houses, item, n)
        time += abs(position - i)
        i = position

print(time)
