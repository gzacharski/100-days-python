from menu import menu
from resources import resources

profit = 0

print(menu)
print(resources)


def is_enough_resources(coffee: str, left_resources) -> bool:
    selected_coffee = menu[coffee]
    ingredients = selected_coffee['ingredients']
    water = ingredients['water']
    milk = ingredients['milk']
    coffee = ingredients['coffee']

    if water < left_resources['water']:
        print("Sorry there is not enough water.")
        return False

    if milk < left_resources['water']:
        print("Sorry there is not enough water.")
        return False

    if coffee < left_resources['coffee']:
        print("Sorry there is not enough water.")
        return False

    return True


def calculate_coins() -> float:
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    sum_of_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    print(f"Money inserted {sum_of_money}")
    return sum_of_money


def process_transaction(money_in_coins: float, money_required: float) -> bool:
    return True


def make_a_coffee(selected_coffee, left_resources):
    print(f"Here is your {selected_coffee}. Enjoy!")
    return True


def report_current_resources():
    print("")


while True:
    decision = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if decision == "off":
        print("Goodbye")
        break

    elif decision == "report":
        report_current_resources()

    elif decision in ["espresso", "latte", "cappuccino"]:
        if not is_enough_resources(decision, resources):
            break
        money_inserted = calculate_coins()

        if not process_transaction(1.00, 1.00):
            break

        resources = make_a_coffee(decision, resources)
    else:
        print("error")
