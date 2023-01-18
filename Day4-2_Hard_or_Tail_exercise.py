#Heads 와 Tails를 랜덤하게 출력하는 방법
import random


#if문으로 구현하는 방법
number = random.randint(0,1)
if number == 0:
    print("Heads")
else : 
    print("Tails")


#리스트로 구현하느 방법
list = ["Heads","Tails"]
saikoro = random.choice(list)
print(saikoro)