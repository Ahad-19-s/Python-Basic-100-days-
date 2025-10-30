x=4
print(x)

def hello():
    global x
    x=100

    print(f"the local number x is{x}")
    print("ahad is a good boy")

     
print(f"the gobal variable {x}")
hello()
print(f"the gobal variable {x}")