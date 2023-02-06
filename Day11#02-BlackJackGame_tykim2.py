import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
pc_cards = []



def append_card(someonecard):
    return someonecard.append(random.choice(cards))

append_card(user_cards)
append_card(user_cards)
append_card(pc_cards)
append_card(pc_cards)

def balckjack():
    print(f"your card : {user_cards}, current score = {sum(user_cards)}")
    print(f"Computer's first card : {pc_cards[0]}")
    print(f"pc card : {pc_cards}, current score = {sum(pc_cards)}")
    if sum(user_cards) == 21 or sum(pc_cards)  == 21:
        print (f"someone is BLACKJACK. someone WIN")
    elif sum(pc_cards) > 21 or  sum(user_cards) > 21 :
        print (f"someone is over. someone WIN")
    elif sum(pc_cards) == 21 and  sum(user_cards) == 21 :
        print (f"Draw")
    elif sum(pc_cards) < 21 and  sum(user_cards) < 21 :
        more_card = input("Type 'y' to get another card, type 'n' to pass : ")
        if more_card == "y":
            append_card(user_cards)
            append_card(pc_cards)
            balckjack()
        elif more_card == "n":
            if sum(user_cards) > sum(pc_cards):
                print("You win")
            elif sum(user_cards) == sum(pc_cards):
                print("Draw")
            else :
                print("You lose")
balckjack()