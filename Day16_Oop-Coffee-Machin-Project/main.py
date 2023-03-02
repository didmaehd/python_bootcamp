from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# 1 print report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



# 2 check resources sufficient
# 3 process Coins
# 4 check transaction successful?
# 5 Make Coffee
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report(),money_machine.report()
    elif choice == "refill":
        if money_machine.refill_payment() :
            coffee_maker.refill()
    else :
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
