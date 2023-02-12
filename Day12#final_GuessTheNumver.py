#강의 따라하기
from random import randint
from Day12_art import logo
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#유저 추측과 비교 함수
def check_answer(guess,answer,turns):
    if guess > answer :
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else :
        print(f"You got it! The answer is {answer}")

#모드 선택 함수 
def set_diffculty():
    level = input("Choose the diffculty. Type 'hard' or 'easy' : ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS

def game():
    print ("Welcome to the Number Guessing Game!")
    print ("I'm thinkin of a number between 1 and 100.")
    #랜덤 숫자 발행 1-00
    answer = randint(1,100)
    # print (f"The correct answer is {answer}.")
    turns = set_diffculty()
    #유저 추측 숫자 
    guess = 0
    #정답이 아니면 반복

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess : "))
        turns = check_answer(guess,answer,turns)
        #리턴받은 기회수가 0이면 종료
        if turns == 0:
            print(f"You've run out of guesses, you lose. The answer is {answer}")
            return
        elif guess != answer:
            print("Guess again")
game()





