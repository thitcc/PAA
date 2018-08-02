while True:
    n, queries = [int(x) for x in input().split()]

    if n == 0 and queries == 0:
        break

    marbles = []

    for i in range(n):
        marbles.append(int(input()))

    for i in range(queries):

    print(marbles)
