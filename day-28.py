letter="my name is {} and i love football {}"
name="ahad"
game="football"

print(letter.format(name,game))# this method using lod python devloper
# new f string:

print(f"hey l love {{game}} and sabina also love {name} ")

txt = "for only {price: .3f} doller!"
print (txt.format(price=49.44430303))

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))
