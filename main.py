MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0
machine_running = True


def get_money():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    quarters_in = int(input("Insert Quarters: "))
    dimes_in = int(input("Insert Dimes: "))
    nickles_in = int(input("Insert Nickles: "))
    pennies_in = int(input("Insert Pennies: "))
    total_money = (quarters_in * quarters) + (dimes_in * dimes) + (nickles_in * nickles) + (pennies_in * pennies)
    return total_money


def resources_check(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def transaction(money_received, cost):
    if money_received < cost:
        print("Sorry not enough money\n Your money has been refunded")
        return False
    else:
        if money_received > cost:
            change = round(money_received - cost, 2)
            print(f"Here is ${change} dollars in change")
        global money
        money += drink["cost"]
        return True


def make_coffee(drink_ordered, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here's your {drink_ordered}, Enjoy!")


while machine_running:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == 'report':
        print(f"Water:{resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
    elif command == 'off':
        machine_running = False
    else:
        drink = MENU[command]
        if resources_check(drink['ingredients']):
            full_money = get_money()
            if transaction(full_money, drink["cost"]):
                make_coffee(command, drink['ingredients'])
