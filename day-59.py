# def decorate(func):
#     def wrapper(a, b):
#         print("good morning")
#         func(a,b)
#         print("thanks for using this method")
#     return wrapper

# @decorate
# def hello():
#     print("hi i am ahad")

# @decorate
# def add(a, b):
#     print(2 + 4)

# add(2, 3)
# def decorate(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)  # wrapper arguments pass করতে হবে
#         print("Thanks for using this method")
#     return wrapper

# @decorate
# def hello():
#     print("Hi, I am Ahad")

# @decorate
# def add(a, b):
#     print(a + b)

# # Function calls
# hello()
# add(2, 4)
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end-start} seconds")
    return wrapper

@timer
def test():
    for i in range(1000000):
        pass

test()
