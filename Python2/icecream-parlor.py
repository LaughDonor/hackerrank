from itertools import combinations

for _ in range(input()):
    m, n = input(), input()
    flavors = map(int, raw_input().split())
    print ['%d %d' % (flavors.index(x) + 1,flavors[flavors.index(x) + 1:].index(y) + flavors.index(x) + 2) for x,y in combinations(flavors, 2) if x + y == m][0]