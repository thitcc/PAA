def merge(left, right):
    global count
    array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
            count += len(left) - i

    while i < len(left):
        array.append(left[i])
        i += 1

    while j < len(right):
        array.append(right[j])
        j += 1

    return array


def merge_sort(data):

    if len(data) > 1:
        middle = int(len(data) / 2)
        left = merge_sort(data[0: middle])
        right = merge_sort(data[middle: len(data)])
        return merge(left, right)
    else:
        return data


for t in range(int(input())):
    input()
    a = []
    for n in range(int(input())):
        a.append(int(input()))
    count = 0
    merge_sort(a)
    print(count)
