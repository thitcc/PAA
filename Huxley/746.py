L_A, C_A, C_B = [int(x) for x in input().split()]
L_B = C_A

matA = []

for i in range(0, L_A):
    matA.append([])
    for j in input().split():
        matA[i].append(int(j))


matB = []

for i in range(0, L_B):
    matB.append([])
    for j in input().split():
        matB[i].append(int(j))

value = 0

for i in range(0, L_A):
    for z in range(0, C_B):
        for j in range(0, C_A):
            value += matA[i][j] * matB[j][z]
        if z == C_B - 1:
            print(value)
        else:
            print(value, end=' ')
        value = 0
