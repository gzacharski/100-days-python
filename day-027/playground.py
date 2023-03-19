def add(num1: int, num2: int = 2) -> int:
    return num1 + num2


def add_2(*args: int) -> int:
    print(type(args))
    result: int = 0
    for arg in args:
        result += arg
    return result


print(add(1, 2))
print(add_2(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        default_kwargs = {'model': 'great-model'}
        kwargs = {**default_kwargs, **kwargs}
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)

print(add(1))
