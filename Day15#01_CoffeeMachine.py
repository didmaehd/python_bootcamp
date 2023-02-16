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


#make coffee
def user_order(order):
    if order == "espresso":
        #리소스가 하나라도 재료보다 적으면 실패 리턴
        #동전에 금액보다 적으면 실패 리턴
        resources["water"] -= MENU[order]["ingredients"]["water"] 
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"] 
        print(f"{order} here!")
    elif order == "latte":
        #리소스가 하나라도 재료보다 적으면 실패
        #동전에 금액보다 적으면 실패
        resources["water"] -= MENU[order]["ingredients"]["water"] 
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"] 
        print(f"{order} here!")
    elif order == "cappuccino":
        #리소스가 하나라도 재료보다 적으면 실패
        #동전에 금액보다 적으면 실패
        resources["water"] -= MENU[order]["ingredients"]["water"] 
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"] 
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
        user_order(order)
#Check resources sufficient
#process coins
#동전 인풋받아서 센트로 합산한 변수 만들기 = 

def check_coins(order, user_coin):
    if user_coin >  MENU[order]["cost"]:
        pass
#check transaction successul

        

