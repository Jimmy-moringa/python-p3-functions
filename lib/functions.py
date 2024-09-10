#!/usr/bin/env python3

def greet_programmer():
    print("Hello, Programmer!")

greet_programmer()





def greet(name):
    print(f"Hello, " + name)


greet("Naureen")



def greet_with_default(name="programmer"):
    print(f"Hello, {name}")

greet_with_default()
greet_with_default("jimmy")


def add(num1, num2):
    return num1 + num2
print(add(57, 65))

# Define the function
def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2


print(halve(46))  


print(halve("two"))  




