
# 함수로 해결

import random
from Day12_art import logo
print(logo)
print ("Welcome to the Number Guessing Game!")
print ("I'm thinkin of a number between 1 and 100.")


#모드에 따른 기회 발급 함수
def attempts(answer):
    if answer == "hard":
        return 5
    elif answer =="easy":
        return 10

# 정답과 유저 추측 비교 함수
def compare(user_guess, correct_answer):
    global start_game
    global your_attempts
    if user_guess == correct_answer :
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


#모드 선택 > 대답에따라 기회수 안내
choose_mode = input("Choose the diffculty. Type 'hard' or 'easy' : ")
your_attempts = attempts(choose_mode)
print(f"You have {your_attempts} attempts remaining to guess the number.")

#1-100사이 랜덤 수 발행 
correct_answer = random.randrange(1,101)
print (f"The correct answer is {correct_answer}.")

#정답과 유저 인풋을 비교하는 함수 호출
#틀릴경우 반복
start_game = True
while start_game : 
    user_guess = int(input("Makr a Guess : "))
    compare(user_guess,correct_answer)






