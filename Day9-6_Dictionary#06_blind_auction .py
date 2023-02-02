# 비밀 경매 강의 따라하기

import os
import Day9_ascii_logo
# os.system('cls')
print(Day9_ascii_logo.logo)
print("Welcome to the secret auction program. ")


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner == bidder
    print(f"The winner is {bidder} with a bid of ${highest_bid}!")    


while not bidding_finished :
    name = input("What is your name? : ")
    price = int(input("What is your bid? : $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. : ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
