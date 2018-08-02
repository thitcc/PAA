def mergeSort(array):
    length = len(array)

    if length <= 1:
        return array

    middle = int(length/2)
    left = mergeSort(array[0:middle])
    right = mergeSort(array[middle:length])


for t in range(int(input())):
    blank = input()
    a = []
    for n in range(int(input())):
        a.append(int(input()))
    print(mergeSort(a))
