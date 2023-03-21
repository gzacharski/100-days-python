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
