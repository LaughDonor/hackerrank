__author__, (N, M) = "LaughDonor", map(int, raw_input().split())
print sum((b - a + 1) * k for _ in xrange(M) for a, b, k in [map(int, raw_input().split())]) / N