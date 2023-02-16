import random

random_int = random.randint(1,100)
print(random_int)

random_float = random.random()
print(random_float*5)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")


list = ["Head","Tail"]
saikoro = random.choice(list)
print(saikoro)

#Heads 와 Tails를 랜덤하게 출력하는 방법
import random


#if문으로 구현하는 방법
number = random.randint(0,1)
if number == 0:
    print("Heads")
else : 
    print("Tails")


#리스트로 구현하는 방법
list = ["Heads","Tails"]
saikoro = random.choice(list)
print(saikoro)