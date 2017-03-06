__author__ = "LaughDonor"
t, a = input(), set(raw_input())
for b in (set(raw_input()) for _ in xrange(t - 1)):
  a = a.intersection(b)
print len(a)