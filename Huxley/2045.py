def merge(a, temp, left, mid, right):
    inv = 0
    i = left
    j = mid

    while i <= mid-1 and j <= right:
        if a[i] < a[j]:
            i += 1
            temp.append(a[i])
        else:
            j += 1
            temp.append(a[j])
            inv += mid - i

    while i <= mid - 1:
        i += 1
        temp.append(a[i])

    while j <= right:
        j += 1
        temp.append(a[j])

    for left in range(left, right):
        a[left] = temp[left]

    return inv


def merge_sort(a, temp, left, right):

    inv = 0

    if left < right:
        mid = int((left + right) / 2)
        inv = merge_sort(a, temp, left, mid)
        inv += merge_sort(a, temp, mid+1, right)
        inv += merge(a, temp, left, mid+1, right)

    return inv


for t in range(int(input())):
    blank = input()
    a = []
    temp = []
    for n in range(int(input())):
        a.append(int(input()))
    print(merge_sort(a, temp, 0, len(a)-1))
