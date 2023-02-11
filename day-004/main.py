import random
import my_module

random_integer = random.randint(100, 200)
print(random_integer)
print(my_module.pi)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

state1 = "Delaware"
state2 = "Pensylwani"

states_of_america = ["Delaware", "Pennsylvania"]
states_of_america.append("Angeland")
print(states_of_america)
print(states_of_america + ["dasd","21"])
print(states_of_america.extend(["dasd", "dawws"]))
