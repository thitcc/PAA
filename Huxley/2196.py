def test(array, middle):
    x = 0
    for i in array:
        if i > middle:
            x += i - middle
    return x


def binary_search(array, begin, end, area):
    middle = 0

    while begin < end:
        middle = (begin + end) / 2
        cut = test(array, middle)
        if cut > area:
            begin = middle + 1E-6
        elif cut < area:
            end = middle - 1E-6
        else:
            break

    print('%.4f' % middle)


n, a = [int(x) for x in input().split()]

while n != 0 and a != 0:

    height = [int(x) for x in input().split()]
    total = sum(height)
    if total == a:
        print(":D")
    elif total < a:
        print("-.-")
    else:
        binary_search(height, 0, max(height), a)

    n, a = [int(x) for x in input().split()]
