MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 500,
    "milk": 500,
    "coffee": 500,
}


def check_coins(order, coin):
    print(order,coin,MENU[order]["cost"])
    if coin <  MENU[order]["cost"] :
        return "fail_money"
    else :
        check_resources (order)

def check_resources (order):
    if resources["water"] < MENU[order]["ingredients"]["water"] or resources["coffee"] < MENU[order]["ingredients"]["coffee"] or resources["milk"] < MENU[order]["ingredients"]["milk"] :
        return "fail_resources"
    else :
        return order

user_coin = 0
run_coffee = True
while run_coffee :
    user_coin == user_coin
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        run_coffee = False
    elif order == "report":
        for i in resources:
            print(f"{i} : {resources[i]}")
        print(f"Money : {user_coin}")
    else :
        coin_list = ["quarters", "dimes","nickles","pennies"]
        for coin in coin_list:
            coins = int(input(f"How namy {coin} ? : "))
            user_coin += coins
        result =(check_coins(order,user_coin))
        
        if result == "fail_money":
            print ("Not enough Money")
            run_coffee = False
        elif result == "fail_resources":
            print ("Not enough resouces")
            run_coffee = False
        elif order :
            resources["water"] -= MENU[order]["ingredients"]["water"] 
            resources["coffee"] -= MENU[order]["ingredients"]["coffee"] 
            resources["milk"] -= MENU[order]["ingredients"]["milk"] 
            user_coin -= MENU[order]["cost"]
            print(f"Here is ${user_coin} in change.")
            print(f"{order} here!")