#조건문으로 구현


import random
import os
import Day14logo
from Day14Data import data

a = random.choice(data)
data.remove(a)

win_point = 0
start_game = True
while start_game :
    b = random.choice(data)
    data.remove(b)
    print ("This is CheatKey",a["follower_count"], b["follower_count"])
    guess = input(
f"""Compare A : {a["name"]}, {a["description"]}, {a["country"]}
Against B : {b["name"]}, {b["description"]}, {b["country"]}
Who has more followers? Type 'A' or 'B' : 
"""
    )
    if guess == "A":
        if a["follower_count"] > b["follower_count"] :
            win_point += 1
            print(f"정답!! {win_point}문제째 정답입니다.")
        else :
            print (f"오답입니다. 당신의 점수는 {win_point}점 입니다.")
            start_game = False
    elif guess == "B":
        if a["follower_count"] > b["follower_count"]  :
            print (f"오답입니다. 당신의 점수는 {win_point}점 입니다.")
            start_game = False
        else :
            win_point += 1
            print(f"정답!! {win_point}문제째 정답입니다.")
            a = b