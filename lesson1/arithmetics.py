x=int(input())
y=int(input())
z=float(input())
print(x,y,z)
print(x+y+z)
print(x*y*z)
print(round(x*z))
print(x/z)
print(x//z)
print(x%y)
print(y**z)
print(((x+y)*(x+z)*(z+y))**3)
print('%.5f' % z)
FLOATS=0
if type(x+y+z)==float:
    FLOATS+=1
if type(x*y*z)==float:
    FLOATS+=1
if type(round(x*z))==float:
    FLOATS+=1
if type(x/z)==float:
    FLOATS+=1
if type(x//z)==float:
    FLOATS+=1
if type(x%y)==float:
    FLOATS+=1
if type(y**z)==float:
    FLOATS+=1
if type(((x+y)*(x+z)*(z+y))**3)==float:
    FLOATS+=1
if type('%.5f' % z)==float:
    FLOATS+=1
print('FLOATS=',FLOATS)
print(x,y,z)


