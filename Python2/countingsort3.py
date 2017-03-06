from bisect import bisect
nums = sorted([int(raw_input().split()[0]) for _ in range(input())])
for n in range(100):
    print bisect(nums,n),