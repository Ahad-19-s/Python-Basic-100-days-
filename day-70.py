class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string_data):
        name, age = string_data.split('-')
        return cls(name, int(age))  # creates a new object

# Create object using normal constructor
s1 = Student("Ahad", 20)

# Create object using alternative constructor
s2 = Student.from_string("Rafi-19")

print(s1.name, s1.age)
print(s2.name, s2.age)
 