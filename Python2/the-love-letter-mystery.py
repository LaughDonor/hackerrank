__author__ = "LaughDonor"
for s in (list(raw_input()) for _ in xrange(input())):
    print sum(abs(ord(s[i]) - ord(s[-1 - i])) for i in range(0,len(s) / 2))