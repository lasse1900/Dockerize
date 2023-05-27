# from counting import counting
import time

def greet(name):
    print("Test")
    counting()
    return f"Hello, {name}!"


def counting():
    for i in range(5):
        print(i)
        time.sleep(1)
    print("I have reached the END !!")

print(greet("John"))
