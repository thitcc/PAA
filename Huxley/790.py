def buildMemo():  # Memo matrix builder
    m = [-1] * (items + 1)

    for i in range(items):
        m[i] = [-1] * (capacity + 1)

    return m


def backpack(i, cc):
    if memo[i][cc] != -1:
        return memo[i][cc]  # Return if this operation has already been processed

    if i == (items - 1) or cc == 0:  # All items have already been visited or backpack is full
        memo[i][cc] = 0
    elif weight[i] > cc:  # Item does not fit in backpack
        memo[i][cc] = backpack(i + 1, cc)
    else:
        memo[i][cc] = max(price[i] + backpack(i + 1, cc - weight[i]), backpack(i + 1, cc))

    return memo[i][cc]


items, capacity = [int(x) for x in input().split()]

price = [int(x) for x in input().split()]  # Item price
weight = [int(x) for x in input().split()]  # Item weight
memo = buildMemo()  # Memo matrix for DP

print(backpack(0, capacity))


