def sort_numbers(s):
    sorts = 0
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j + 1] = s[j]
            j = j - 1
            sorts += 1
        s[j + 1] = val
    return sorts

input()
print sort_numbers(map(int,raw_input().split()))