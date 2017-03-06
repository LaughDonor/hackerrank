__author__, P, ret = "LaughDonor", input() ^ input(), 1
while(P): # this one takes O(log N) steps
    ret <<= 1
    P >>= 1
print ret - 1