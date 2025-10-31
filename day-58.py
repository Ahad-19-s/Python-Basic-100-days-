class Dog:
    def __init__(self, name="sifat", age=33, gf="mashiat"):
        self.name = name
        self.age = age
        self.gf = gf
        print("create an a object")

    def info(self):
        print(f"My name is {self.name}. Today using class and object")
        print(self.age, self.gf)

# Object creation
a = Dog("Ahad", 35, "Sabina")
b = Dog("Nahid", 34, "Tammana")
c = Dog()  # Will use default values

# Accessing info
a.info()
b.info()
c.info()

