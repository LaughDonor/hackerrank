__author__ = "LaughDonor"
for N, stockPrices, maxProfit, shares in ((input(), map(int, raw_input().split()), 0, 0) for _ in xrange(input())):
    optimalPrices = [0] * (N - 1) + stockPrices[-1:]
    for i in xrange(N - 2, -1, -1):
        optimalPrices[i] = max(stockPrices[i], optimalPrices[i + 1])
    for i in xrange(N):
        if i == N - 1 or optimalPrices[i + 1] < optimalPrices[i]:
            # sell all shares
            maxProfit += shares * optimalPrices[i]
            shares = 0
        elif stockPrices[i] < optimalPrices[i]:
            # buy one share
            shares += 1
            maxProfit -= stockPrices[i]
    print maxProfit