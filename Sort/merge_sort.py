def merge(left, right):
    total = len(left) + len(right)
    array = []
    i = 0
    j = 0

    for k in range(total):
        if j == len(right) or i < len(left) and left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1

    return array


def merge_sort(data):
    length = len(data)

    if length <= 1:
        return data

    middle = int(length / 2)
    left = merge_sort(data[0: middle])
    right = merge_sort(data[middle: length])

    return merge(left, right)