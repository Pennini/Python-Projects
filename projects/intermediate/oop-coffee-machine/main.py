from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while True:
    order = input(f"  What would you like? ({menu.get_items()}): ")

    if order == "report":
        coffee.report()
        money.report()
    elif order == "off":
        print("Maintenance")
        break
    else:
        drink = menu.find_drink(order)
        if drink != None  and coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)