def distribution(array, size):
    global people
    slices = 0

    for bread in array:
        slices += int(bread / size)
        if slices >= people:
            return True

    return False


def search(array, begin, end):
    global result

    if begin <= end:
        middle = int((begin + end) / 2)
        if distribution(array, middle):
            if middle > result:
                result = middle
            search(array, middle+1, end)
        else:
            search(array, begin, middle-1)


people = int(input())
sandwich = int(input())

a = [int(x) for x in input().split()]
a.sort()

result = 0
search(a, a[0], a[len(a)-1])

print(result)
