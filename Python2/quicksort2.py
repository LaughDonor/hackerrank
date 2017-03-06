__author__, _ = "LaughDonor", input()

def quickSort(A):
    if not A:
        return A
    a, b, x = [], [], A.pop(0)
    for i in A:
        a.append(i) if i < x else b.append(i)
    A = quickSort(a) + [x] + quickSort(b)
    if len(A) > 1:
        print ' '.join(map(str, A))
    return A

quickSort(map(int, raw_input().split()))