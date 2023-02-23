programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A place of code that you can easily call over and over again",
    "Loop": 'the action of doing something over and over again'
}

print(programming_dictionary)
print(programming_dictionary["Function"])

programming_dictionary["Variable"] = "a placeholder for some value"

for key in programming_dictionary.keys():
    print(programming_dictionary[key])

empty_dictionary = {}

for entry in programming_dictionary.items():
    print(entry)

# wipe the existing dictionary
programming_dictionary = {}

print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer"

for entry in programming_dictionary.items():
    print(entry)
