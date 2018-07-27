n,m = map(int, input().split())
n = int(n)
m = int(m)
g = input().split()
w = input().split()
c = 0
i=j=0
for i in range(len(g)):
    try:
        if(int(w[0]) >= int(g[i])):
            c+=1
            del w[0]
    except Exception as e:
        pass
print(c)
