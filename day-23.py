l=[11,3,45,5,2,2,5,323]
print(l)
l.append(2)
print(l)
l.sort() # revarae mathod
l.sort(reverse=True)
print(l)
print(l.index(3))
print(l.count(2))

m=l
m[0]=0
print(l)
m.insert(2,33)
print(l)
a=["ahad","sabu"]
m.extend(a)
print(l)


