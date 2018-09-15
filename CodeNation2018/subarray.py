# https://www.hackerrank.com/contests/codeagon/challenges/bob-and-subarray-or
t = int(input().strip())

L = list(map(int, input().strip().split()))
k = [L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)]
s = 0
for i in range(len(k)):
    a = k[i]
    o = 0
    for j in range(len(a)):
        o = o | a[j]
    s+=o
print(s)
