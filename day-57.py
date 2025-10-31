class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
# print(acc.__balance)    # Error! Private variable

# Parent class
class Animal:
    def eat(self):
        print("Eating...")

# Child class
class Dog(Animal):
     def bark(self):
        print("Barking...")

d = Dog()
d.eat()   # Eating... (inherited)
d.bark()  # Barking...
