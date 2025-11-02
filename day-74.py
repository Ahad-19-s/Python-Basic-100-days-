# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greet(self):
#         print("Hello from Child")  # Overrides parent method

# # Create objects
# p = Parent()
# c = Child()

# p.greet()  # Hello from Parent
# c.greet()  # Hello from Child
# Method Overriding কী?

# Definition:

# যখন একটি child class তার parent class-এর কোনো method কে পুনরায় define করে, একই নাম এবং parameter ব্যবহার করে, তখন তাকে method overriding বলে।

# ✔️ অর্থাৎ, child class-এ method থাকলে Python child class-এর method কে প্রাধান্য দেয়, parent class-এর method নয়।


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side   # Overrides Shape.area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

shapes = [Square(4), Circle(3)]

for shape in shapes:
    print(shape.area())
