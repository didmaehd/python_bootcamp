import random
import os
from Day11_art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def compare(user_score,computer_score):
    if user_score == computer_score :
        return("Draw")
    elif computer_score == 0:
        return("Lose, opponent has Blackjack")
    elif user_score == 0:
        return("You Win with a Blackjack")
    elif user_score > 21 :
        return("You lose, you went over")
    elif computer_score > 21 :
        return("Win, opponent went over.")
    elif user_score > computer_score :
        return("You win")
    else :
        return("Oppenent win")

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return "BlackJack!"
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game() :
    print (logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False :
        user_socre = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print (f"Your cards : {user_cards}, current score : {user_socre}")
        print (f"Computer's first card : {computer_cards[0]}")
        if user_socre == 0 or computer_score == 0 or user_socre > 21 : 
            is_game_over = True
        else :
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            elif user_should_deal == "n":
                is_game_over = True

    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print (f"Your final hand : {user_cards} , final socre {user_socre}")
    print (f"Opponent final hand : {computer_cards} , final socre {computer_score}")
    print (compare(user_socre,computer_score))

while input ("Do you want to play a Blackjack? Type 'y' or 'n' : " ) == "y":
    os.system("cls")
    play_game()
