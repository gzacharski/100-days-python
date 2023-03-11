# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as names_file:
    names = [name.strip() for name in names_file.readlines()]

for name in names:
    new_letter = letter.replace("[name]", name)
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_to_{name.lower()}.txt", mode="w") as letter_to:
        letter_to.write(new_letter)
