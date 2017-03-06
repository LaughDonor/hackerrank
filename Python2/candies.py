__author__, N = "LaughDonor", input()
candy, ratings = [1] * (N + 1), [input() for x in xrange(N)] + [0]

for i, c in enumerate(candy[1:N], 1):
    left, mid, right = ratings[i - 1:i + 2]
    if left < mid:
        c = candy[i - 1] + 1
    elif left > mid:
        j = i
        while i > 0 and ratings[j - 1] > ratings[j]:
            candy[j - 1] = max(candy[j - 1], candy[j] + 1)
            j -= 1
    else:
        c = 1
    candy[i] = c

print sum(candy) - 1