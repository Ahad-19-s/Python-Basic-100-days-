class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, name):
        self.__name = name

    # Getter with validation
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

p = Person("Ahad", 25)
print(p.get_name())  # Ahad
p.set_name("Nahid")
print(p.get_name())  # Nahid

p.set_age(-5)         # Invalid age
print(p.get_age())    # 25



class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age")

p = Person("Ahad", 25)
print(p.name)   # Ahad
p.name = "Nahid"
print(p.name)   # Nahid

p.age = -5      # Invalid age
print(p.age)    # 25
