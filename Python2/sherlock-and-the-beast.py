__author__ = "LaughDonor"
for N, x, y in ((input(), 0, 0) for _ in xrange(input())):
	while (N - 5 * x) % 3 and y >= 0:
		x += 1
		y = (N - 5 * x) / 3
	y = (N - 5 * x) / 3
	print -1 if y < 0 else '5' * (3 * y) + '3' * (5 * x)