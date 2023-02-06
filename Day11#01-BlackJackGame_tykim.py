import random

money = 500

number_list = [1,2,3,4,5,6,7,8,9,10]
my_first_card = random.choice(number_list) 
my_second_card = random.choice(number_list)
my_point = my_first_card + my_second_card

pc_first_card = random.choice(number_list) 
pc_second_card = random.choice(number_list)
pc_point = pc_first_card + pc_second_card

continue_game = True
while continue_game:
    bets = int(input("Place Your Bets : "))

    print(f"Your fist card is {my_first_card} second card is {my_second_card} Your Point is {my_point}")
    print(f"PC's Second card is {pc_second_card }")

    if my_point == 21 or pc_point > 21 :
        print( "YOU BALCKJACK! YOU Win!")
        money += bets
        print (f"Your Money is {money}")
    if my_point > 21 or pc_point == 21:
        print(f"Your point is {my_point}. PC Win!")
        money -= bets
        print (f"Your Money is {money}")
    select = input("SELECT 'HIT' or 'STAND' : ")
    if select == "HIT":
        next_card = random.choice(number_list)
        my_point += next_card
        if my_point > 21 :
            print(f"Your card is {next_card}.Your point is {my_point}. PC Win!")
            money -= bets
            print (f"Your Money is {money}")
        elif my_point == 21 :
            print(f"Your card is {next_card}. Your point is {my_point}. YOU BALCKJACK! YOU Win!")
            money += bets
            print (f"Your Money is {money}")
        else :
            print(f"Your card is {next_card}. Your point is {my_point}.")
    elif select == "STAND":
        if my_point > pc_point:
            print(f"Your point is {my_point} and PC point {pc_point}")
            print("You win")
            money += bets
            print (f"Your Money is {money}")
        elif my_point == pc_point:
            print("DRAW")
        else:
            print(f"Your point is {my_point} and PC point {pc_point}")
            print("PC WIN")
            money -= bets
            print (f"Your Money is {money}")
