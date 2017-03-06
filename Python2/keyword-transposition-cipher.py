__author__, AZ = "LaughDonor", 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def uniq(S):  # Get unique, preserving order
    seen = set()
    return [x for x in S if x not in seen and not seen.add(x)]

for W, C, alpha in ((uniq(raw_input()), raw_input(), list(AZ)) for _ in xrange(input())):
    map(alpha.remove, W)  # Remove all characters in W from the alpha set
    for i, c in enumerate(alpha):
        W[i % len(W)] += c
    W = ''.join(sorted(W))
    print ''.join(chr(W.index(x) + 65) if x != ' ' else ' ' for x in C)