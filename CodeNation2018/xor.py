# https://www.hackerrank.com/contests/codeagon/challenges/xor-queries
t = int(input().strip())

for i in range(t):
    q = list(map(int, input().strip().split()))
    x = q[0]
    l = q[1]
    r = q[2]
    max  = 0
    for y in range(l, r+1):
        re = x^y
        print(x, y, re)
