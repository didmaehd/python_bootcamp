# 함수의 리턴값에따라 아웃풋 만들어보기

import random
import os
from Day14logo import logo
from Day14logo import vs
from Day14Data import data

win_point = 0
start_game = True
data1 = random.choice(data)
data.remove(data1)

def compare (a,b,c):
    global win_point
    global start_game
    if c == "A":
        if a["follower_count"] > b["follower_count"] :
            return "successa"
        else :
            return "fail"
    elif guess == "B":
        if a["follower_count"] > b["follower_count"]  :
            return "fail"
        else :
            return "successb"

while start_game :
    data2 = random.choice(data)
    data.remove(data2)
    print ("This is CheatKey",data1["follower_count"], data2["follower_count"])
    guess = input(
f"""{logo}
Compare A : {data1["name"]}, {data1["description"]}, {data1["country"]}
{vs}
Against B : {data2["name"]}, {data2["description"]}, {data2["country"]}
Who has more followers? Type 'A' or 'B' : 
""")

    compare (data1,data2,guess)

    result = compare (data1,data2,guess)
    if result == "successa":
        win_point += 1
        os.system("cls")
        print (f"You're right! Current score {win_point}.")
    elif result == "successb":
        win_point += 1
        os.system("cls")
        print (f"You're right! Current score {win_point}.")
        data1 = data2
    else :
        os.system("cls")
        print (f"Sorry that's wrong. Final score {win_point}.")
        start_game = False

