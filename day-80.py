# Multilevel Inheritance মানে হলো —
# একটা child class যদি একটা parent class থেকে inherit করে,
# আর সেই parent class আবার অন্য একটা grandparent class থেকে inherit করে —
# তখন তাকে বলে Multilevel Inheritance।

# অর্থাৎ, Inheritance-এর চেইন তৈরি হয়।
# Base Class
class Grandfather:
    def property(self):
        print("Grandfather: Owns a big house.")

# Intermediate Class
class Father(Grandfather):
    def car(self):
        print("Father: Owns a car.")

# Derived Class
class Son(Father):
    def laptop(self):
        print("Son: Owns a laptop.")
# Object of Son
s = Son()
s.property()   # From Grandfather
s.car()        # From Father
s.laptop()     # From Son
