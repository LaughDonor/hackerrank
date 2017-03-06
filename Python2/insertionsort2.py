def sort_numbers(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j + 1] = s[j]
            j = j - 1
        s[j + 1] = val
        print ' '.join(map(str,s))
input()
sort_numbers(map(int,raw_input().split()))