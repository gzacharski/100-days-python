import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

actions = [rock, paper, scissors]

selected_action = input("Choose action: rock, paper or scissors. Type [r], [p] or [s]").lower()
the_action = rock

if selected_action == 'r':
    the_action = rock
elif selected_action == 'p':
    the_action = paper
elif selected_action == 's':
    the_action = scissors
else:
    print("There is no matching action.")
    exit()

print("You select:")
print(the_action)

print("Computer selects: ")
random_action = actions[random.randint(0, len(actions) - 1)]
print(random_action)

if the_action == random_action:
    print("Nobody wins")
elif the_action == rock:
    print("Computer won") if random_action == paper else print("You won")
elif the_action == paper:
    print("Computer won") if random_action == scissors else print("You won")
elif the_action == scissors:
    print("Computer won") if random_action == rock else print("You won")
