# Multiple Inheritance মানে হলো —
# 👉 যখন একটা child class একাধিক parent class থেকে inherit করে।

# অর্থাৎ, একটা ক্লাস একসাথে দুই বা ততোধিক ক্লাসের features পায়।
# Parent Class 1
class Father:
    def skills(self):
        print("Father: Knows driving and gardening.")

# Parent Class 2
class Mother:
    def skills(self):
        print("Mother: Knows cooking and painting.")

# Child Class inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        # Call parent methods using super()
        super().skills()
        print("Child: Knows programming and music.")
c = Child()
c.skills()
