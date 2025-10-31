a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, কারণ মান একই
print(a is b)  # False, কারণ memory আলাদা

 
c=a
print(a is c)
print(c==b)
print("break line" )

# x=2
# y=2
# print(x==y)
# print(x is y)

x=None
print(type(x))
