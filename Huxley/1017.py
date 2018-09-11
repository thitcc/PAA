def fibonacci(x):
    if memo[x] != -1:
        return memo[x]

    if x <= 2:
        f = 1
    else:
        f = fibonacci(x - 1) + fibonacci(x - 2)

    memo[x] = f
    return f


n = int(input())
memo = [-1 for x in range(n + 1)]
memo[0] = 0
memo[1] = 1
print(fibonacci(n - 1))
# n-1 porque a questao é assim
