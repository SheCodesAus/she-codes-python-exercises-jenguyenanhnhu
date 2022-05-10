# Functions have parentheses.

# Defining the function. 
def hello():
    print("Hello world!")

# Calling the function.

def add(x, y):
    result = x + y
    return result

print(add(36, 43))


def create_greeting(name):
    greeting = f"Hello, {name}"
    return greeting

print(create_greeting("Chilli"))
print(create_greeting("Ivy"))
print(create_greeting("Remus"))


def triple(number):
    return 3*number

print(triple(10))


def convert_cm_to_in(length_cm):
    length_in_inches = length_cm / 2.54
    return length_in_inches

print(convert_cm_to_in(25))


def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean

print(calculate_mean(7, 6))