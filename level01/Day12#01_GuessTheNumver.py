
#if + while문으로 해결

import random
from Day12_art import logo
print(logo)
print ("Welcome to the Number Guessing Game!")
print ("I'm thinkin of a number between 1 and 100.")

#모드 선택 > 대답에따라 기회수 안내
choose_mode = input("Choose the diffculty. Type 'hard' or 'easy' : ")
def attempts(answer):
    if answer == "hard":
        return 5
    elif answer =="easy":
        return 10
your_attempts = attempts(choose_mode)
print(f"You have {your_attempts} attempts remaining to guess the number.")

#1-100사이 랜덤 수 발행 
correct_answer = random.randrange(1,101)
print (f"The correct answer is {correct_answer}.")

#유저 인풋 받음 -> 비교 및 처리 -> 반복 -> 남은 기회 0이면 종료
start_game = True
while start_game : 
    user_guess = int(input("Makr a Guess : "))
    if user_guess == correct_answer:
        print(f"You got it! The answer is {correct_answer}")
        start_game = False
    else :
        if user_guess > correct_answer:
            print(f"Too high")
        elif user_guess < correct_answer:
            print(f"Too low")
        your_attempts -= 1
        print(f"You have {your_attempts} attempts remaining to guess the number.")
        if your_attempts == 0 :
             print("You've run out of guesses, you lose.")
             start_game = False
        else:
            print("Try again.")





    # elif user_guess > correct_answer:
    #     print(f"Too high")
    #     your_attempts -= 1
    #     print(f"You have {your_attempts} attempts remaining to guess the number.")
    #     if your_attempts == 0 :
    #          print("You've run out of guesses, you lose.")
    #          start_game = False
    #     else:
    #         print("Try again.")
    # elif user_guess < correct_answer:
    #     print(f"Too low")
    #     your_attempts -= 1
    #     print(f"You have {your_attempts} attempts remaining to guess the number.")
    #     if your_attempts == 0 :
    #          print("You've run out of guesses, you lose.")
    #          start_game = False
    #     else:
    #         print("Try again.")
