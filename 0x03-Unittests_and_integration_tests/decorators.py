import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("function is changed")
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

def say_hello():
    print("Hello")

say_hello()

@my_decorator
def say_hello(name):
    print(f"Hello {name}")
    return "h"

s = say_hello("abrham")
