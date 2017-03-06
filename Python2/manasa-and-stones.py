__author__ = "LaughDonor"
for s, N, A, B in ((set(), input(), input(), input()) for _ in xrange(input())):
    for i in xrange(N):
        s.add(i * A + (N - i - 1) * B)
    print ' '.join(map(str, sorted(list(s))))