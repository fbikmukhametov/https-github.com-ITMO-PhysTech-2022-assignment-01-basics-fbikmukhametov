import random
x=random.randint(1,10)
y=random.randint(1,10)
shagi=0
print(x,y)
if x-y>0:
    print(x-y-1)
else:
    print(y-x-1)
while x>1:
    if x%2:
        x=x//2
        shagi=shagi+1
    else:
        x=3*x+1
        shagi=shagi+1
print('количесвто шагов =',shagi)

