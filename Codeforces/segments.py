# http://codeforces.com/contest/1015/problem/A

n, m = map(int, input().split())
li = []
for i in range(n):
    l,r = map(int, input().split())
    li.append(l)
    li.append(r)
# print(li)
c = 0
li2 = []
f= 0
for j in range(1,m+1):
    for k in range(0,len(li)-1,2):
        if (j >= li[k] and j <= li[k+1]):
            f = 0
            break
        else:
            f = 1
    if(f == 1):
        c+=1
        li2.append(j)
print(c)
for s in range(len(li2)):
    print(li2[s], end= ' ')
