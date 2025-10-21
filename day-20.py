a=4
v=3

def calculator(a,b):
    mean = (a*b)/(a+b) 
    print (mean)

calculator(a,v)

def isgreater(a,b):
    if(a>b):
        print("first number is greater than")
    else:
        print("second number is greater than")
        
isgreater(a,v)

def isleaer(a,v):
    pass

# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")
