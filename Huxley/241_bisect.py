from bisect import bisect_left


def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i

    return -1


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
        result = index(marbles, query)
        if result > -1:
            print("{} found at {}".format(query, result+1))
        else:
            print("{} not found".format(query))
