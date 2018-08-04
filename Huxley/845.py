def cut(array, tree):
    global k
    pieces = 0

    for n in array:
        sub = n - tree
        if sub > 0:
            pieces += sub

    k += 1

    return pieces


def search(array, begin, end):
    global result
    global woods

    if begin <= end:
        middle = int((begin + end) / 2)
        pieces = cut(array, array[k])
        if pieces >= woods:
            result = array[k-1]
            search(array, middle+1, end)
        else:
            search(array, begin, middle-1)


size, woods = [int(x) for x in input().split()]

treeHeight = []

for i in input().split():
    treeHeight.append(int(i))

treeHeight.sort()
k = 0
result = 0
search(treeHeight, treeHeight[0], treeHeight[size-1])
print(result)
