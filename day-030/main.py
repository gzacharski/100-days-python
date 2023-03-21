# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")
    # a_dictionary = {"key": "value"}
    # print(a_dictionary["dasda"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    print("There was an error")
except KeyError as error_message:
    print(f"There key {error_message} does not exist.")
else:
    print("There were no exceptions")
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file was closed")
    # raise TypeError("This is an error I made up")

height = float(input("height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
