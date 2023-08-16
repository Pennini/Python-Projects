from replit import clear
from biblio_intermediate import MENU

stop_machine = False
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def check_resources(order):
    global resources
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {item}. Wait a second.")
            resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
            }
            return False
    else:
        return True


def process_coin():
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(order):
    for item in resources:
        resources[item] -= order[item]
    print("Here is your espresso ☕️. Enjoy!")


def transaction(decision, total):
    global profit
    cost = decision["cost"]
    if total >= cost:
        total -= cost
        profit += cost
        print(f"Here is ${total:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while True:
    decision = input("{  What would you like? (espresso/latte/cappuccino): "}).lower()
    while (
        decision != "espresso"
        and decision != "latte"
        and decision != "cappuccino"
        and decision != "report"
        and decision != "off"
    ):
        clear()
        decision = input("  Sorry, what would you like? (espresso/latte/cappuccino): ")

    if decision == "off":
        print("Maintenance")
        break

    if decision == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Milk: {resources['milk']}g")
        print(f"Money: ${profit}")
    else:
        choice = MENU[decision]
        if check_resources(choice["ingredients"]):
            change = process_coin()
            if transaction(choice, change):
                make_coffee(choice["ingredients"])

