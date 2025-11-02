class Employee:
    def __init__(self,nam,age,id):
        self.name=nam
        self.age1=age
        self.ID=id

    def showdetails(self):
        print(f"the emplyeee name id {self.ID} is the name of {self.name} and also his {self.age1} old years")



class Mannager(Employee):
    def showlanguage (self):
        print("this is a in heritance")

first_employee=Employee("ahad",23,1986)
first_employee.showdetails()
second = Mannager("sabina",33,1987)
second.showdetails()
second.showlanguage()
# multilevel inheritance 

class ceo(Mannager):
    def showmaltiplee (self):
        print(f"this is the most userful inharitance {self.name}")

t=ceo("sifat",23,1986)
t.showmaltiplee()

# multiple class inharitancce 
class A:
    def feature1(self):
        print("Feature 1")

class B:
    def feature2(self):
        print("Feature 2")

class C(A, B):   # Multiple Inheritance
    def feature3(self):
        print("Feature 3")

obj = C()
obj.feature1()
obj.feature2()
obj.feature3()
#  hierarchical inheritance 
class Parent:
    def show(self):
        print("Parent feature")

class Child1(Parent):
    def feature1(self):
        print("Child 1 feature")

class Child2(Parent):
    def feature2(self):
        print("Child 2 feature")

obj1 = Child1()
obj2 = Child2()
obj1.show()
obj2.show()


# there are some type inharitance are mixied  so called are the hybrid inheritance
class A:
    def feature1(self):
        print("A feature")

class B(A):
    def feature2(self):
        print("B feature")

class C(A):
    def feature3(self):
        print("C feature")

class D(B, C):  # Hybrid form
    def feature4(self):
        print("D feature")

obj = D()
obj.feature1()
obj.feature4()
