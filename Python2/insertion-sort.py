"""
TEST CASES PASSED:  4
TEST CASES FAILED:  0
TEST CASES TIMEOUT: 6
SCORE: 6.48 / 50
"""
def sort_numbers(s):
    sorts = 0
    for i in xrange(1, len(s)):
        val, j = s[i], i - 1
        while (j >= 0) and (s[j] > val):
            s[j + 1], j = s[j], j - 1
            sorts += 1
        s[j + 1] = val
    return sorts

for _ in xrange(input()):
    input()
    print sort_numbers(map(int, raw_input().split()))
