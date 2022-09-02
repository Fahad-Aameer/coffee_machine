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
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
espresso_cost = 1.5
latte_cost = 2.5
cappuccino_cost = 3.0
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


while machine_running:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == 'report':
        print(f"Water:{water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}")
    if command == 'off':
        machine_running = False
    if command == 'espresso':
        if water < 50 or coffee < 18:
            print("Sorry there is not enough resources.")
        else:
            full_money = get_money()
            if full_money < espresso_cost:
                print("Sorry not enough money\n Your money has been refunded")
            else:
                get_change = round(full_money - espresso_cost, 2)
                if full_money > espresso_cost:
                    print(f"Here is ${get_change} dollars in change")
                money += espresso_cost
                water -= 50
                coffee -= 18
                print("Here's your Espresso, Enjoy!")
    elif command == 'latte':
        if water < 200 or milk < 150 or coffee < 24:
            print("Sorry there is not enough resources.")
        else:
            full_money = get_money()
            if full_money < latte_cost:
                print("Sorry not enough money\n Your money has been refunded")
            else:
                get_change = round(full_money - latte_cost, 2)
                if full_money > latte_cost:
                    print(f"Here is ${get_change} dollars in change")
                money += latte_cost
                water -= 200
                milk -= 150
                coffee -= 24
                print("Here's your Latte, Enjoy!")
    elif command == 'cappuccino':
        if water < 250 or milk < 100 or coffee < 24:
            print("Sorry there is not enough resources.")
        else:
            full_money = get_money()
            if full_money < cappuccino_cost:
                print("Sorry not enough money\n Your money has been refunded")
            else:
                get_change = round(full_money - cappuccino_cost, 2)
                if full_money > cappuccino_cost:
                    print(f"Here is ${get_change} dollars in change")
                money += cappuccino_cost
                water -= 250
                milk -= 100
                coffee -= 24
                print("Here's your Cappuccino, Enjoy!")
