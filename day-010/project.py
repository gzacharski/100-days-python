from art import logo

print(logo)


# Calculator

# add
def add(a: int, b: int):
    return a + b


# subtract
def subtract(a: int, b: int):
    return a - b


# multiply
def multiply(a: int, b: int):
    return a * b


# divide
def divide(a: int, b: int):
    if b == 0:
        print("You cant divide by zero!")
        return
    return a / b
