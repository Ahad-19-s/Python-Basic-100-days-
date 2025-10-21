tup= (23,4,4)

print(tup.count(4))
print(type(tup))
for i in tup:
    print(i)

# manupulate by tuple
temp=list(tup)
temp.append([23,333,2,44,22,111])
print(temp)