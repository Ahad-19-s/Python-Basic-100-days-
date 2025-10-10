#create a calculator using python
# print(5+6)
# print(15-6)
# print(15*6)
# print(15/6)
# print(15//6)
# print(5%3)
# print(2**4)

num1=float(input ("Enter first number : "))
operator=input("Enter operator(+,-,*,/): ")
num2=float(input("enter the number second number : "))

if operator == '+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator == '/':
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operator!"

print(f"Result :{num1} {operator} {num2}={result}")
name = "Ahad"
print(f"My name is {name}")
