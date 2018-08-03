def divisions(array, middle, people):
    divisions = 0

    for i in array


def search(array, people, begin, end):
    begin = 0
    end = len(array) - 1

    if begin <= end:
        middle = int((begin + end) / 2)
        if divisions(array, middle):
            if middle > resp:
                resp = middle



    return -1


people = int(input())
sandwich = int(input())

cent = [int(x) for x in input().split()]

cent.sort()

print(search(cent, people, cent[0], cent[sandwich-1]))


