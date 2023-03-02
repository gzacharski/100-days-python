from menu import menu
from resources import resources

profit = 0


def prompt_question_to_user():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def print_report_of_current_resources():
    print(f"Water: {the_resources['water']}ml")
    print(f"Milk: {the_resources['milk']}ml")
    print(f"Coffee: {the_resources['coffee']}g")
    print(f"Money: ${the_resources['money']}")


def is_enough_resources(coffee: str) -> bool:
    selected_coffee = menu[coffee]
    ingredients = selected_coffee['ingredients']
    water = ingredients.get('water')
    milk = ingredients.get('milk', 0)
    coffee = ingredients.get('coffee', 0)

    if water > the_resources['water']:
        print("Sorry there is not enough water.")
        return False

    if milk > the_resources['water']:
        print("Sorry there is not enough milk.")
        return False

    if coffee > the_resources['coffee']:
        print("Sorry there is not enough coffee.")
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
    if money_in_coins < money_required:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_in_coins > money_required:
        print(f"Here is ${money_in_coins - money_required} dollars in change.")

    the_resources['money'] += money_required
    return True


def make_a_coffee(selected_coffee):
    ingredients = menu.get(selected_coffee).get('ingredients')
    the_resources['water'] -= ingredients.get('water', 0)
    the_resources['milk'] -= ingredients.get('milk', 0)
    the_resources['coffee'] -= ingredients.get('coffee', 0)
    print(f"Here is your {selected_coffee}. Enjoy!")


the_resources = resources
while True:
    decision = prompt_question_to_user()

    if decision == "off":
        print("Goodbye")
        break

    elif decision == "report":
        print_report_of_current_resources()

    elif decision in ["espresso", "latte", "cappuccino"]:
        if not is_enough_resources(decision):
            break
        money_inserted = calculate_coins()
        money_required = menu.get(decision).get('cost')
        if not process_transaction(money_inserted, money_required):
            break

        make_a_coffee(decision)
    else:
        print("error")
