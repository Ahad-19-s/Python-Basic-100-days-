import os
class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello!")

s1 = Student("Ahad", 20)

print(dir(Student))
print ("dictonary")
print(Student.__dict__)
print(s1.__dict__)     
print("help fuction")  
help(Student)
# 1️⃣ dir() — কোনো object-এর attributes ও methods দেখতে
# 👉 কাজ:

# dir() ফাংশন কোনো object, class, module, function বা variable-এর সব attributes ও methods-এর নামের list রিটার্ন করে।__dict__ — object বা class-এর ভিতরে থাকা data (namespace)
# 2️⃣ __dict__ — object বা class-এর ভিতরে থাকা data (namespace)
# 👉 কাজ:

# __dict__ হলো একটা dictionary যা কোনো object বা class-এর attributes ও তাদের মান (values) ধারণ করে।
