

user_coin = 0
coin_list = ["quarters", "dimes","nickles","pennies"]
for coin in coin_list:
    coins = int(input(f"How namy {coin} ? : "))
    if coin == "quarters":
        user_coin = coins * 25
    if coin == "dimes":
        user_coin = user_coin + coins * 10
    if coin == "nickles":
        user_coin = user_coin + coins * 5
    if coin == "pennies":
        user_coin = user_coin + coins * 2.5

print (user_coin)