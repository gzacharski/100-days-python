def greet():
    print("hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


greet()


def greet_with_name(name=""):
    print(f"hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Grzegorz")


def greet_with(name="", location=""):
    print(f"hello {name}")
    print(f"What is it like in {location}?")


greet_with("Grzegorz", "Warsaw")
greet_with(location="Warsaw", name="Grzegorz")
