__author__ = "LaughDonor"
for N, C, M in (map(int, raw_input().split()) for _ in xrange(input())):
    Total_Chocolates = N / C
    Wrappers = Total_Chocolates

    while Wrappers / M:  
        Chocolates = Wrappers / M  
        Wrappers = Wrappers % M + Chocolates  
        Total_Chocolates += Chocolates
    print Total_Chocolates