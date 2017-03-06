from collections import Counter
__author__ = "LaughDonor"
#Get the Counter of all letters, then get the counter of how many times they appear based on odd/even.
#If any odd values appear more than once, then it can't be a palindrome
print ["YES", "NO"][Counter(i % 2 for i in Counter(raw_input()).values())[1] > 1]