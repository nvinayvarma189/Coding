# https://www.codechef.com/LOCJUN18/problems/CHEFCUP
t = int(input())
for i in range(0,t):
    a = int(input())
    b = int(input())
    val = 0
    for x in range(1, min(a,b)):
        v = a*b*x - a*x**2 - b*x**2 + x**3
        print(v)
        break
        if (val > v):
            print(x-1,val)
            break
        val = v
