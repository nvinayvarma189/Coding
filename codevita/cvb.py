# The casino has introduced a new game in which there are M vertical chutes each
# containing N single digit (possibly zero)
# numbers. You can choose any chute and draw the bottom number and when you do this all
# the other numbers in the chute descend by one slot.
# You need to build the largest integer using this process drawing all the numbers from the chutes.
# For example, in the following example, we have three chutes of four numbers each and the largest number that can be drawn is 469534692781.
# Given the number of chutes and the numbers in each chute, write a program to find the largest integer that could be formed using the above process.
'''
TestCase 1
4,4

7,5,5,2

3,6,1,7

8,7,0,4

8,7,3,9



9743782557163078

TestCase 2
2,3

1,2,3

2,4,6

643221
'''

def same(y):
    return all(a == -1 for a in y)
m = int(input())
n = int(input())
l = m*n
num = []
for i in range(0, l):
    a = int(input())
    num.append(a)
s = ""
y = []
for i in range(l-1, 0, -n):
    y.append(num[i])
while True:
    if (same(y)):
        break
    else:
        m = max(y)
        t = (len(num)-1) - n*(y.index(m))
        for i in range(0,n-1):
            num[t] = num[t-1]
            t-=1
        num[t] = -1
        y =[]
        for i in range(l-1, 0, -n):
            y.append(num[i])
        s = s+str(m)
print(s)
