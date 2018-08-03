def bs_left(array, element):
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


tests = 0

while True:
    n, queries = [int(x) for x in input().split()]

    if n == 0:
        break
    else:
        tests += 1

    marbles = []

    for i in range(n):
        marbles.append(int(input()))
    marbles.sort()

    print('CASE# {}:'.format(tests))

    for i in range(queries):
        query = int(input())
        result = bs_left(marbles, query)
        if result > -1:
            print("{} found at {}".format(query, result + 1))
        else:
            print("{} not found".format(query))
