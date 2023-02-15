import random
import os
from Day14logo import logo
from Day14logo import vs
from Day14Data import data

def compare (a,b,c):
    global data1
    global data2
    global win_point
    global start_game
    if guess == "A":
        if data1["follower_count"] > data2["follower_count"] :
            win_point += 1
            os.system("cls")
            print (f"You're right! Current score {win_point}.")
        else :
            print (f"Sorry that's wrong. Final score {win_point}.")
            start_game = False
    elif guess == "B":
        if data1["follower_count"] > data2["follower_count"]  :
            print (f"Sorry that's wrong. Final score {win_point}.")
            start_game = False
        else :
            win_point += 1
            data1 = data2
            os.system("cls")
            print (f"You're right! Current score {win_point}.")
data1 = random.choice(data)
data.remove(data1)

win_point = 0
start_game = True
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
"""
    )
    compare (data1,data2,guess)