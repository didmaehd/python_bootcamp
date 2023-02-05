# 비밀 경매 프로그램 생성

import os
import Day9_ascii_logo
# os.system('cls')
print(Day9_ascii_logo.logo)

print("Welcome to the secret auction program. ")
end_game = True
user_dict = {}
while end_game :
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    user_dict[name] = bid
    judgment = input("Are there any other bidders? Type 'yes' or 'no'. : ")
    if judgment == "yes":
        os.system('cls')
    else:
        end_game = False

bid = 0
winner = "o"
for name in user_dict:
    if user_dict[name] > bid :
        bid = user_dict[name]
        winner =  name
print(f"The Winner is [{winner}] with the bid of ${bid}!! ")