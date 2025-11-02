class A:
    def show(self):
        print("Class A")

class B(A):
    def sho(self):
        super().show()
        print("Class B")

class C(B):
    def sho(self):
        super().show()
        print("Class C")

obj = C()
obj.show()
