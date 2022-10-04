s1=str(input())
s2=str(input())
s3=''
s4=''
print('длина строк=',len(s1)*len(s2))
print(s1,s2)
print(s1,',',s2)
print("Hello,",s1,'!Just wanted to say:',s2)
i=0
while s1[i]!=' ':
    s3=s3+s1[i]
    i=i+1
i=0
while s2[i]!=' ':
    s4=s4+s2[i]
    i=i+1
print(s3,s4)
k=1
for i in range(len(s1)):
    if s1[i]==' ':
        k=k+1
print('кол-во слов в первой строке=', k)
if s1 in s2:
    sum=0
    i=0
    while s2[i]!=s1[0]:
        i=i+1
    for n in range(len(s1)):
        if s2[i+n]==s1[n]:
            sum=sum+1
        if sum==len(s1):
            print(i)
