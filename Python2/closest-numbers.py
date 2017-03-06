from itertools import combinations
input()
nums = sorted(map(int,raw_input().split()))
smallest = 2000000
small = []
for n in range(1,len(nums)):
    ab = nums[n]-nums[n-1]
    if smallest > ab:
        smallest = ab
        small = []
    if smallest == ab:
        small.extend([nums[n-1],nums[n]])

print ' '.join(map(str,small))