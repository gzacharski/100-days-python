from art import logo, vs
from game_data import data
import random, os


def swap_with_last(index):
    length = len(data)
    temp = data[length - 1]
    data[length - 1] = data[index]
    data[index] = temp


def draw_celebrity(length):
    index = random.randint(0, length)
    return data[index], index


def draw_celebrities_to_compare():
    celeb_1, index_1 = draw_celebrity(len(data) - 1)
    swap_with_last(index_1)
    celeb_2, _ = draw_celebrity(len(data) - 2)
    return celeb_1, celeb_2


def print_celebrities(celebrity_1, celebrity_2):
    print(f"Compare A: {celebrity_1['name']}, {celebrity_1['description']}, from {celebrity_1['country']}.")
    print(vs)
    print(f"Compare B: {celebrity_2['name']}, {celebrity_2['description']}, from {celebrity_2['country']}.")


score = 0

while True:
    os.system('cls')
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    celebrity_1, celebrity_2 = draw_celebrities_to_compare()
    print_celebrities(celebrity_1, celebrity_2)

    decision = input("Who has more followers? Type 'A' or 'B': ")
    if decision.lower() == 'a' and celebrity_1['follower_count'] > celebrity_2['follower_count']:
        score += 1
    elif decision.lower() == 'b' and celebrity_1['follower_count'] < celebrity_2['follower_count']:
        score += 1
    else:
        break

print(f"Sorry, that's wrong. Final score: {score}")
