
i = True
coin_list = ["quarters", "dimes","nickles","pennies"]
while i :
    for coin in coin_list:
        coins = int(input(f"How namy {coin} ? : "))
        if coin == "quarters":
            a = coins * 25
        if coin == "dimes":
            b = coins + coins * 10
        if coin == "nickles":
            c = coins + coins * 5
        if coin == "pennies":
            d = coins + coins * 2.5
    user_coin = a+b+c+d
    print (user_coin)

