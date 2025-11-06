# 1️⃣ Hierarchical Inheritance in Python
# 🧠 Definition:

# যখন একটি Parent Class থেকে একাধিক Child Class inherit করে,
# তখন তাকে বলে Hierarchical Inheritance।

# অর্থাৎ —
# একটা “বাবা” (Parent Class), অনেকগুলো “ছেলে” (Child Classes)।
# Parent Class
class Parent:
    def show_parent(self):
        print("This is the Parent class.")

# Child Class 1
class Child1(Parent):
    def show_child1(self):
        print("This is the First Child class.")

# Child Class 2
class Child2(Parent):
    def show_child2(self):
        print("This is the Second Child class.")
# Create objects
c1 = Child1()
c2 = Child2()

c1.show_parent()
c1.show_child1()

c2.show_parent()
c2.show_child2()
# Hybrid Inheritance মানে হলো —
# একটা প্রোগ্রামে একসাথে একাধিক type of inheritance (যেমন single, multiple, multilevel, hierarchical) মিশ্রিতভাবে থাকা।

# অর্থাৎ এটি হলো combination of different inheritance types।
# Base Class
class A:
    def feature_a(self):
        print("Feature A from Class A")

# Derived from A
class B(A):
    def feature_b(self):
        print("Feature B from Class B")

# Derived from A
class C(A):
    def feature_c(self):
        print("Feature C from Class C")

# Derived from both B and C (Multiple + Multilevel)
class D(B, C):
    def feature_d(self):
        print("Feature D from Class D")
obj = D()
obj.feature_a()  # from A
obj.feature_b()  # from B
obj.feature_c()  # from C
obj.feature_d()  # from D
