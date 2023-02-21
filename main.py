
i = True
cent = 0
coin_list = ["quarters", "dimes","nickles","pennies"]
while i :
    for coin in coin_list:
        coins = int(input(f"How namy {coin} ? : "))
        if coin == "quarters":
            cent = cent + coins * 25
        if coin == "dimes":
            cent =  cent + coins * 10
        if coin == "nickles":
            cent =  cent + coins * 5
        if coin == "pennies":
            cent =  cent + coins * 2.5
    print (cent)

