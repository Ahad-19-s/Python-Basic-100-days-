def cube(x):
    return x*x*x

print(cube(4))

l=[1,2,3,4,5]
newl=[]

for item in l:
    newl.append(cube(item))

print(newl)


double = list(map(cube,l))
print(double)
fil=lambda x: x%2==0

fi= list(filter(fil,l))
print(fi)

s = lambda x,y: x + y
from functools import reduce
a = reduce(s, l)
print(a)
