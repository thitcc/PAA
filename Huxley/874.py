import sys
sys.setrecursionlimit(50000)


def topDown(size):
    if memo[size] != -1:
        return memo[size]

    result = -1
    for i in range(size+1):
        total = prices[i] + topDown(size - i - 1)
        result = result if result > total else total

    memo[size] = result

    return memo[size]


n = int(input())

while n != 0:
    prices = [int(input()) for x in range(n)]
    memo = [-1 for x in range(n)]
    memo[0] = prices[0]
    print(topDown(n - 1))
    n = int(input())
