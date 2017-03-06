for _ in range(input()):
    n,k = map(int, raw_input().split())
    print "YES" if all([(x + y >= k) for x,y in zip(sorted(map(int, raw_input().split())),sorted(map(int, raw_input().split()), reverse=True))]) else "NO"