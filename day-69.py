class Student:
    school_name = "ABC High School"   # Class variable

    def __init__(self, name):
        self.name = name              # Instance variable

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name    # Change class variable

# Using the class method
# Student.change_school("XYZ International School")

# Creating objects
s1 = Student("Ahad")
s2 = Student("Rafi")
s1.change_school("New Model School")   # Works fine
print(s1.school_name)
print(s2.school_name)




print(Student.school_name)
