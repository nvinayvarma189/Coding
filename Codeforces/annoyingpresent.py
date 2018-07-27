n,m = map(int, input().split())
m = int(m)
n = int(n)
i = n//2+1
l= []
for a in range(n):
    l.append(0)
print(l)
x,d = map(float, input().split())
x = float(x)
d = float(d)
sum = x+d
for j in range(m):
    prod = d*abs(i - j)
    prod = float(prod)
    print(prod)
    l[j] = sum+prod
print(l)
