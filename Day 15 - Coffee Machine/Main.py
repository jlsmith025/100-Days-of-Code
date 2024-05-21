

import sys
from setup import resources
from setup import menu

def produce_report(money):
    print('Water: ' + str(resources["water"]) + 'ml')
    print('Milk: ' + str(resources["milk"]) + 'ml')
    print('Coffee: ' + str(resources["coffee"]) + 'g')
    print('Money: $' + str(money))

def money_provided():
    total = 0
    total += int(input("How many quarters?")) * .25
    total += int(input("How many dimes?")) * .10
    total += int(input("How many nickels?")) * .05
    total += int(input("How many pennies?")) * .01
    return total

def give_change(total, cost):
    change = round(total - float(cost), 2)
    print(f"Here is {change} in change.")

def verify_drink_resources(drink_type):
    enough_resources = True

    for ingredient in menu[drink_type]['ingredients']:
        #print(resources[ingredient])
        #print(menu[drink_type]['ingredients'][ingredient])
        if menu[drink_type]['ingredients'][ingredient] > resources[ingredient]:
            print(f"There is not enough {ingredient}")
            enough_resources = False
    return enough_resources

def dispense_drink(drink_type):
    for ingredient in menu[drink_type]['ingredients']:
        resources[ingredient] -= menu[drink_type]['ingredients'][ingredient]

    print(f"Here is your {drink_type} ☕. Enjoy!")


def machine():
    money = 0.0
    machine_status = 'on'

    while machine_status == 'on':
        selection = input("What would you like? (espresso/latte/cappuccino):")

        if selection.lower() == 'report':
            produce_report(money)
        elif selection.lower() == 'off':
            machine_status = 'off'
            sys.exit()
        elif selection.lower() in menu:
            if verify_drink_resources(selection.lower()):
                total = money_provided()
                if total >= menu[selection.lower()]["cost"]:
                    money += menu[selection.lower()]["cost"]
                    give_change(total, menu[selection.lower()]["cost"])
                    dispense_drink(selection.lower())
                else:
                    print("Sorry that's not enough money. Money refunded.")



machine()