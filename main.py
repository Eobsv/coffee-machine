import data

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# TODO Print report, water, coffee, milk, money
# TODO Coins 1,5,10,25
# TODO Process coins
# TODO Check the transaction
# TODO Make a coffee
# TODO Refer to .pdf file downloaded. To be found in GoogleChrome PythonTabGroup


profit = 0
water = data.resources["water"]
coffee = data.resources["coffee"]
milk = data.resources["milk"]


def print_report():
    print(f"Money: ${profit}, water: {water}ml, coffee: {coffee}g, milk: {milk}ml")


def is_resource_sufficient(order_ingredients):
    """Returns True if order ingredients are sufficient if not False"""
    for item in order_ingredients:
        if order_ingredients[item] >= data.resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_succesful(money_received, drink_cost):
    """True if payment is accepted, False if there is not enough money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the req. ingredients from the resources"""
    for item in order_ingredients:
        data.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "Report":
        print_report()
    else:
        drink = data.MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])