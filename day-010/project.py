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


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

number_1 = int(input("What is the first number? "))
number_2 = int(input("What is the second number? "))
for symbol in operations.keys():
    print(f"Type {symbol} for {operations[symbol].__name__}.")

operation = str(input("What operation do you want to do? "))
if not operation in operations:
    print(f"There is no such an operation like: {operation}.")
    exit()

func = operations[operation]
result = func(number_1, number_2)
print(f"{number_1} {operation} {number_2} = {result}")
