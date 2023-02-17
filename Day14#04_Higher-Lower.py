#강의 따라하기

import random
import os
from Day14logo import logo ,vs
from Day14Data import data

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def chcek_answer(guess,a_followers,b_followers):
    if guess == "a":
        if a_followers > b_followers:
            return "success_a"
        else :
            return False
    if guess == "b":
        if a_followers > b_followers:
            return False
        else :
            return "success_b"
    # if a_followers > b_followers:
    #     return guess == "guess"
    # else:
    #     return guess == "b"

print(logo)
score = 0
account_a = random.choice(data)

game_should_continue = True
while game_should_continue :
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    print(a_followers_count,b_followers_count)
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    os.system("cls")
    is_correct = chcek_answer(guess,a_followers_count,b_followers_count)

    if is_correct == "success_a":
        score += 1
        print (f"You're right! Current score : {score}")
    elif is_correct == "success_b":
        score += 1
        account_a = account_b
        print (f"You're right! Current score : {score}")
    else :
        game_should_continue = False
        print(f"Sorry, that's wrong. final score : {score}")


