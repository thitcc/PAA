import sys
sys.setrecursionlimit(15000)


def cuttingRod(n):
    if memo[n] != -1:
        return memo[n]

    best_price = -1

    for i in range(n):
        total_cut_price = prices[i] + cuttingRod(n - i - 1)
        best_price = best_price if best_price > total_cut_price else total_cut_price

    memo[n] = best_price

    return memo[n]


n = int(input())

while n != 0:
    prices = [int(input()) for x in range(n)]
    memo = [-1 for x in range(n + 1)]
    memo[0] = 0  # size 0 has no price
    print(cuttingRod(n))
    n = int(input())
