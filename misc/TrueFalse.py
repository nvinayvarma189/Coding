# Enter your code here. Read input from STDIN. Print output to STDOUT


'''You and your friend have just taken a True/False Test. Your friend has been to see the instructor, sothey know how man answers they got right
(but not which ones). You compate.
notes: you know your answers and your friend's answers. What is the maximum number of answers you could have gotten right? '''

'''
Each input will consist of a single test case. Note that your program may be run multilple times on different inputs. Each test case wil begin
with a line containing a single integer n (0<= n <= 1000) which is the number of answer your friend got righton the exam. Each of the next two
lines will contain a string s (max[n,1]<= |s| <= 1000, s belongs to {T,F}*). The two strings will be of the same length. The first line respresnts
your friend;s answers and the second line represents your answers. The order of answers is the same in both strings. The first letter is 
asnwer for the 1st question, Second letter is answer for the 2nd question and son on...

Output:
Output a single integer, which is the maximum number of asnwers you could have gotten right?


Sample input 1:
3
FTFFF
TFTTT

Sample output 1:
2

Sample input 2:
6
TTFTFFTFTF
TTTTFFTTTT

Sample output 2:
9
'''

import itertools

n = int(input())
y = input()
f = input()

count = n
substringsf = []
substringsy = []
substringsfnot = []
substringsynot = []

index = [x for x in range(len(y))]
listin = []
for item in itertools.combinations(index, n):
substringsf.append(item)
    for i in (index):
        if i not in (item):
substringsfnot.append(i)



for item in itertools.combinations(index, n):
substringsy.append(item)
    for i in index:
        if i not in (item):
substringsynot.append(i)




countlist = []
s= 0    
for i in range(len(substringsf)):
c= 0
    for j in range(n):
        if y[substringsf[i][j]] == f[substringsy[i][j]]:
c+=1
    for k in substringsfnot[s:s+(len(y)-n)]:
        if y[k] != f[k]:
c+=1
s+=(len(y)-n)
countlist.append(c)

print(max(countlist))
