
# Parent Class
class Parent:
    def show_parent_info(self):
        print("I am the Parent class.")

# Child Class inherits from Parent
class Child(Parent):
    def show_child_info(self):
        print("I am the Child class.")

# Create object of Child
obj = Child()

# Access method from Parent class
obj.show_parent_info()

# Access method from Child class
obj.show_child_info()
