#강의 따라하기
from random import randint
from Day12_art import logo
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#유저 추측과 비교 함수
def check_answer(guess,answer,turns):
    if guess > answer :
        print("高いよ")
        return turns -1
    elif guess < answer:
        print("低いよ")
        return turns -1
    else :
        print(f"正解だよ！ {answer}")

#모드 선택 함수 
def set_diffculty():
    level = input("レブルを選択してね. Type 'hard' or 'easy' : ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS

def game():
    print ("ようこそ！数位あてゲームへ!")
    print ("1から100の間の数字をすいそくしてね.")
    #랜덤 숫자 발행 1-00
    answer = randint(1,100)
    # print (f"The correct answer is {answer}.")
    turns = set_diffculty()
    #유저 추측 숫자 
    guess = 0
    #정답이 아니면 반복

    while guess != answer:
        print(f"のこりチャンスは {turns} 回だよ！がんばって！.")
        guess = int(input("数字を入力して : "))
        turns = check_answer(guess,answer,turns)
        #리턴받은 기회수가 0이면 종료
        if turns == 0:
            print(f"もうチャンスはなくなったね, きみの負けだ！. 答えは {answer}だよ")
            return
        elif guess != answer:
            print("もういちど！")
game()





