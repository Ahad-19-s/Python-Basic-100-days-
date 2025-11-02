# Example: Magic Methods in One Class

class MyCollection:
    """
    This class demonstrates multiple Magic/Dunder Methods in Python.
    """

    def __init__(self, items):
        """Constructor (__init__) - called when object is created"""
        self.items = items            # instance variable

    def __str__(self):
        """String representation (__str__) - called by print(obj)"""
        return f"MyCollection with items: {self.items}"

    def __len__(self):
        """Length (__len__) - called by len(obj)"""
        return len(self.items)

    def __getitem__(self, index):
        """Indexing (__getitem__) - called by obj[index]"""
        return self.items[index]

    def __setitem__(self, index, value):
        """Set item (__setitem__) - called by obj[index] = value"""
        self.items[index] = value

    def __delitem__(self, index):
        """Delete item (__delitem__) - called by del obj[index]"""
        del self.items[index]

    def __add__(self, other):
        """Addition (__add__) - called by obj1 + obj2"""
        return MyCollection(self.items + other.items)

    def __eq__(self, other):
        """Equality (__eq__) - called by obj1 == obj2"""
        return self.items == other.items

    def __call__(self, msg):
        """Callable (__call__) - allows obj() like a function"""
        print(f"MyCollection says: {msg}")

    def __contains__(self, item):
        """Contains (__contains__) - called by 'item in obj'"""
        return item in self.items


# -------------------------------
# Using the MyCollection class
# -------------------------------

col1 = MyCollection([1, 2, 3])
col2 = MyCollection([4, 5])

# __str__
print(col1)                # MyCollection with items: [1, 2, 3]

# __len__
print(len(col1))           # 3

# __getitem__ and __setitem__
print(col1[1])             # 2
col1[1] = 20
print(col1[1])             # 20

# __delitem__
del col1[0]
print(col1)                # MyCollection with items: [20, 3]

# __add__
col3 = col1 + col2
print(col3)                # MyCollection with items: [20, 3, 4, 5]

# __eq__
print(col1 == col2)        # False
print(col1 == MyCollection([20, 3]))  # True

#
