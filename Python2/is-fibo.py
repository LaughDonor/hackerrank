__author__ = "LaughDonor"
for N in (input() for _ in xrange(input())):
    r1, r2 = (5 * n ** 2 + 4) ** 0.5, (5 * n ** 2 - 4) ** 0.5
    print "Is%sFibo" % ("Not" if r1 % 1 and r2 % 1 else "")