class Student:
    school_name = "ABC School"    # 🏫 Class variable (shared by all)

    def __init__(self, name, marks):
        self.name = name          # 👤 Instance variable
        self.marks = marks        # 👤 Instance variable

# Create two objects
s1 = Student("Ahad", 90)
s2 = Student("Tuhin", 85)

# Change instance variable
s1.marks = 95
print(s1.marks)  # 95
print(s2.marks)  # 85  (unchanged)

# Change class variable using class name
Student.school_name = "XYZ School"
print(s1.school_name)  # XYZ School
print(s2.school_name)  # XYZ School
s1.school_name = "PQR School" 
s1.school_name = "PQR School" #লিখলে Python নতুন একটা instance variable বানিয়ে ফেলে
# — এটা আর class variable না!
# তাই শুধু s1 অবজেক্টে প্রভাব পড়ে, ক্লাসে না।
print(s1.school_name)  # PQR School
print(s2.school_name)  # XYZ School
print(Student.school_name)  # XYZ School



print(s1.name, s1.school_name)
print(s2.name, s2.school_name)
