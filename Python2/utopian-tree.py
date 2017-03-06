__author__ = "LaughDonor"
for N in (input() for _ in xrange(input())):
    print pow(2, (N + 1) / 2 + 1) - 1 - (N % 2)