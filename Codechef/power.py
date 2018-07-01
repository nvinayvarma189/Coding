# https://www.codechef.com/problems/SUMPOWER
t=int(input())
for i in range(0,t):
    n = int(input())
    k = int(input())
    s = input()
    sum = 0
    for j in range(1, n-k+1):
        o = j
        i = o-1
        p = 0
        for l in range(0,k):
            if (s[i+l] != s[o+l]):
                p += 1
        sum  += p
    print(sum)
