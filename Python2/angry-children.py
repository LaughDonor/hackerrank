__author__, N, K = "LaughDonor", input(), input()
A, ans = sorted(input() for _ in xrange(N)), 1e9

for i in xrange(N - K + 1):
	ans = min(ans, A[i + K - 1] - A[i])
print ans