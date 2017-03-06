__author__, N, K, sigma = "LaughDonor", input(), input(), 0
A, val = sorted(input() for _ in xrange(N)), 1 - K
sumA = [A[0]]
for i, a in enumerate(A[1:]):
    sumA.append(sumA[i] + a)

for i in xrange(K):
    sigma += val * A[i]
    val += 2

ans = sigma
for i in xrange(K, N):
    new = sigma + (K - 1) * (A[i] + A[i - K]) - 2 * (sumA[i - 1] - sumA[i - K])
    ans, sigma = min(new, ans), new

print ans