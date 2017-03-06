__author__, N, A = "LaughDonor", input(), map(int, raw_input().split())
sigma, prod = sum(A), sum(A[i] * (i + 1) for i in xrange(N))
max_prod = prod
for i in xrange(N):
    prod += sigma - A[-1 - i] * N
    max_prod = max(max_prod, prod)
print max_prod