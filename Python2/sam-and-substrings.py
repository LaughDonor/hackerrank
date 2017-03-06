__author__, S, ten, sigma = "LaughDonor", map(int, list(raw_input())), 1, 1
N, tot, MOD = len(S), len(S) * S[-1], lambda x: x % 1000000007
for i in xrange(N - 1, 0, -1):
    ten = MOD(ten * 10)
    sigma += ten
    tot = MOD(tot + (sigma * i) * S[i - 1])
print MOD(tot)