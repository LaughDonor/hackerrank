__author__, (N, T), width = "LaughDonor", map(int, raw_input().split()), map(int, raw_input().split())
for i, j in (map(int, raw_input().split()) for _ in xrange(T)):
	print min(width[i:j + 1])