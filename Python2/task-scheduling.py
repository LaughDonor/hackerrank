__author__, nl = "LaughDonor", []
time = length = late = 0
def returnIndex(array, number):
    if not array:
        return None
    if len(array) == 1:
        return 0 if number > array[0] else None

    return binarySearch(array, number, 0, len(array) - 1)

def binarySearch(array, number, si, ei):
    if si == ei:
        return si - (number < array[si])
    middle = (ei - si) // 2 + si
    if number > array[middle]:
        return binarySearch(array, number, middle + 1, ei)
    elif number < array[middle]:
        return binarySearch(array, number, si, middle)
    return middle

def addJob(length, array, deadline, minutes, late):
    if length < deadline:
        for i in xrange(deadline - length):
            array.append(i + length)
        length = deadline
    minLeft, index = minutes, returnIndex(array, deadline - 1)
    if index != None:
        while index >= 0 and minLeft > 0:
            array.pop(index)
            index -= 1
            minLeft -= 1

    while minLeft > 0 and array and array[0] < deadline:
        array.pop(0)
        minLeft -= 1
    return late + minLeft, length

for dl, m in (map(int, raw_input().split()) for _ in xrange(input())):
    late, length = addJob(length, nl, dl, m, late)
    print late