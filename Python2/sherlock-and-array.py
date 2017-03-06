"""
TEST CASES PASSED:  4
TEST CASES FAILED:  1
TEST CASES TIMEOUT: 2
SCORE: 13.33 / 40
"""
def solution(nums):
    for n in xrange(1,len(nums) - 1):
        s1, s2 = sum(nums[:n]), sum(nums[n + 1:])
        if s1 == s2:
            return "YES"
        if s1 > s2:
            break
    return "NO"
for _ in xrange(input()):
    input()
    nums = map(int, raw_input().split())
    print solution(nums)