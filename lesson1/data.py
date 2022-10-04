import random
n=int(input())
a=[]
for i in range(n):
    a.append(random.randint(1,10))
#print(a[0],a[n//2],a[n-1])
max=0
for i in range(n):
    if a[i]>0:
        max=a[i]
min=100
for i in range(n):
    if a[i]<min:
        min=a[i]
print(a)
print(a[0],a[n//2],a[n-1])
print('максимальное значение=',max,'минимальное значение=',min)
s=0
for i in range(n):
    s=s+a[i]
print(s)
b=[]
for i in range(n):
    if a[i]%2==0:
        b.append(a[i]**2)
print(b)
for i in range(n):
    if a[i]==min:
        print(i)
        break
c=[]
for i in range(n):
    if i%2==0:
        c.append(a[i])
print(c)

