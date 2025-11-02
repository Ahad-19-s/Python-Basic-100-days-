# ১️⃣ Public Members

# 👉 এগুলো সব জায়গা থেকে access করা যায় — ক্লাসের ভিতর, বাইরে, এমনকি subclass থেকেও।

# 🔹 Syntax:
# # সাধারণ ভ্যারিয়েবল বা মেথড নাম (কোনো underscore ছাড়া)
class Student:
    def __init__(self, name, age):
        self.name = name       # Public variable
        self.age = age         # Public variable

    def display(self):         # Public method
        print(f"Name: {self.name}, Age: {self.age}")

obj = Student("Ahad", 20)

print(obj.name)     # ✅ Access করা যায়
obj.display()       # ✅ Access করা যায়

# Private Members

# 👉 এগুলো শুধুমাত্র সেই ক্লাসের ভিতরে access করা যায়,
# বাইরে থেকে বা সাবক্লাস থেকেও access করা যায় না।

# 🔹 Syntax:
# দুটি underscore __ দিয়ে শুরু হয়।
class Student:
    def __init__(self, name, roll):
        self.__roll = roll     # Private variable
        self.name = name

    def __show(self):          # Private method
        print(f"Roll: {self.__roll}")

    def display(self):
        self.__show()          # ✅ ক্লাসের ভিতরে access করা যায়

obj = Student("Ahad", 101)
obj.display()

print(obj.name)        # ✅ পাবলিক ভ্যারিয়েবল
print(obj._Student__roll)       # ❌ AttributeError হবে


# গুলো শুধু ক্লাস ও সাবক্লাসের ভিতরে ব্যবহারের জন্য,
# তবে technically বাইরেও access করা যায় (Python এটা জোর করে বন্ধ করে না — কেবল “নিষেধাজ্ঞা”র ইঙ্গিত দেয়)।

# 🔹 Syntax:
# একটি single underscore _ দিয়ে শুরু হয়।

class Student:
    def __init__(self, name, roll):
        self._roll = roll     # Protected variable
        self.name = name

    def _show(self):          # Protected method
        print(f"Roll: {self._roll}")

class SubStudent(Student):
    def display(self):
        self._show()          # ✅ সাবক্লাস থেকে access করা যায়

obj = SubStudent("Ahad", 103231)
obj.display()

# print(obj._roll)   # ⚠️ technically access করা যায়, কিন্তু discourage করা হয়
