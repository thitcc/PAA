def test(ladder, k):
    current = 0

    for step in ladder:
        jump = step - current
        current = step
        if jump > k:
            return False
        elif jump == k:
            k -= 1

    return True


def monkey(ladder, begin, end):
    if begin > end:
        return begin

    k = (begin + end) // 2

    if test(ladder, k):
        return monkey(ladder, begin, k-1)
    else:
        return monkey(ladder, k+1, end)


for t in range(int(input())):
    size = int(input())
    array = [int(x) for x in input().split()]
    array.sort()
    print("Case {}: {}".format(t + 1, monkey(array, array[0], array[size - 1])))
