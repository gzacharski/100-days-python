with open("D:\\udemy\\python\\src\\day-024\\my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("New text.")
    print(contents)

with open("my_new_file.txt", mode="w") as file:
    file.write("New text.")
    print(contents)
