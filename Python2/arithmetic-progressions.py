"""
TEST CASES PASSED:  3
TEST CASES FAILED:  0
TEST CASES TIMEOUT: 6
SCORE: 13.71 / 80
"""
from math import factorial

#Store computed factorials to avoid recalculating
fact = {}
AP = []

for ap in range(input()):
    AP.append(map(int, raw_input().split()))

for op in range(input()):
    operation = map(int, raw_input().split())
    if operation.pop(0) == 0:
        i, j = operation
        #Query
        index = i - 1
        K = 0
        V = 1
        while index < j:
            K += AP[index][2]
            V *= pow(AP[index][1], AP[index][2])
            index += 1
        if K not in fact:
            fact[K] = factorial(K)
        V *= fact[K]
        print('%s %s' % (K, V % 1000003))
    else:
        i, j, v = operation
        #Update
        index = i - 1
        while index < j:
            AP[index][2] += v
            index += 1