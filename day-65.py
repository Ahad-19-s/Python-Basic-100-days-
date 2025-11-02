# Static Method হলো এমন এক ধরনের method যা class-এর মধ্যে থাকে,
# কিন্তু এটা class বা object — কোনো কিছুর state পরিবর্তন করে না।

# অর্থাৎ:

# এটা instance variable (self) ব্যবহার করে না

# এটা class variable (cls) ও ব্যবহার করে না

# এটা শুধুমাত্র utility function এর মতো কাজ করে (class context এর ভিতরে থাকা একধরনের সাধারণ ফাংশন)

# 🧱

class Student:
    school_name = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def welcome_message():
        print("Welcome to the school!")

    def show(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Usage
Student.welcome_message()    # ✅ Class দিয়ে কল করা utility function 
s1 = Student("Ahad", 95)
s1.welcome_message()         # ✅ Object দিয়েও কল করা সম্ভব
s1.show()
