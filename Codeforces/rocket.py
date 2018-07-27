n, q = map(int, input().split())
n = int(n)
q = int(q)
l = input()
k=[]
if(q == 1):
    print(ord(min(l))-96)
else:
    for i in range(len(l)):
        k.append(l[i])
    k = list(set(k))
    li = sorted(k)
    # print(li)
    # print(li)
    i=0
    s= ' '
    # print(s)
    for i in range(len(li)):
        if(ord(s[-1])+1 == ord(li[i])):
            pass
        else:
            s+=li[i]
    # print(s)
    s= s[1:q+1]
    # print(s)
    su = 0
    if(len(s) == q):
        for j in range(len(s)):
            su+=ord(s[j]) - 96
    if(su == 0):
        su = -1
    print(su)
