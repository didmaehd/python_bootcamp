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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources (order):
    if resources["water"] < MENU[order]["ingredients"]["water"] or resources["coffee"] < MENU[order]["ingredients"]["coffee"] or resources["milk"] < MENU[order]["ingredients"]["milk"] :
        print ("Sorry! not enough resources")
    else :
        user_order(order)

def check_coins

#make coffee
def user_order(order):
    if order :
        #동전에 금액보다 적으면 실패 리턴
        #리소스에서 커피 물 우유 양을 빼준다
        resources["water"] -= MENU[order]["ingredients"]["water"] 
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"] 
        resources["milk"] -= MENU[order]["ingredients"]["milk"] 
        print(f"{order} here!")

run_coffee = True
while run_coffee :
#prompt user by asking 
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
#turn off coffee machine 
    if order == "off":
        run_coffee = False
#print report
    elif order == "report":
        for i in resources:
            print(f"{i} : {resources[i]}")
    else :
        check_resources (order)
        # user_order(order)

#Check resources sufficient
#리소스가 하나라도 재료보다 적으면 실패 리턴

#process coins
#동전 인풋받아서 센트로 합산한 변수 만들기 = 

def check_coins(order, user_coin):
    if user_coin >  MENU[order]["cost"]:
        pass
#check transaction successul

        

