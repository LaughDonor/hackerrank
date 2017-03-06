from collections import Counter
input()
a = Counter(raw_input().split())
input()
b = Counter(raw_input().split())
print ' '.join(sorted(b - a))