n, k = map(int, raw_input().split())
nums = dict((int(el), 0) for el in raw_input().split())
print sum([1 for n in nums.keys() if n + k in nums])
