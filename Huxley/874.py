import sys
sys.setrecursionlimit(15000)


def cuttingRod(length):
    if memo[length] != -1:
        return memo[length]

    result = -1
    for i in range(length):
        total = prices[i] + cuttingRod(length - i - 1)
        result = result if result > total else total

    memo[length] = result

    return memo[length]


n = int(input())

while n != 0:
    prices = [int(input()) for x in range(n)]
    memo = [-1 for x in range(n + 1)]
    memo[0] = 0
    print(cuttingRod(n))
    n = int(input())
