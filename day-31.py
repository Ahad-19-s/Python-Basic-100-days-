s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()
print(type(harry))

for value in info:
  print(value)

  s={1,2,2,4,5}
  s2={3,2,4,5,6}

  print(s.union(s2))
  print (s.intersection(s2))
#   s.update(s2)
#   print(s)
  print(s.symmetric_difference(s2))

  info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
  