print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower() + name2.lower()
first = 0
for letter in "true":
    first += names.count(letter)

second = 0
for letter in "love":
    second += names.count(letter)

total = int(f"{first}{second}")

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 <= total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
