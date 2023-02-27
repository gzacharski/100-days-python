# Global scope
player_health = 10

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# variable created in if or while loop does not have another scope
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

variable = 1


def increment():
    # bad habit - error prone
    global variable
    variable += 1
    print(variable)


increment()

# constants
PI = 3.14159
URL = "https://google.com"
