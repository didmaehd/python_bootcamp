import random
#가위 바위 보 ASCII ART 변수 저장
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#input받은 가위,바위,보를 1,2,3 으로 받는다
# 1,2,3,에 해당하는 텍스트를 출력한다 를 출력한다
yourrps = input("Enter your choice 1(Rock), 2(Paper), Scissor(3) : ")
if yourrps == "1":
    print (scissors)
elif yourrps == "2":
    print (rock)
elif yourrps == "3":
    print (paper)

#랜덤한 값을 출력하도록
list = [scissors,rock,paper]
pcrps = random.choice(list)
print(pcrps)


#범위 외
if yourrps != ["1","2","3"] :
    print("정확한 값을 인력하세요.")
#비김
elif yourrps == "1" and pcrps == scissors:
    print("비겼네요.")
elif yourrps == "2" and pcrps == rock:
    print("비겼네요.")
elif yourrps == "3" and pcrps == paper:
    print("비겼네요.")
#내가 가위 - 비김 제외
elif yourrps == "1" and pcrps == rock:
    print("당신이 졌어요")
elif yourrps == "1" and pcrps == paper:
    print("당신이 이겼어요")
#내가 바위 - 비김 제외
elif yourrps == "2" and pcrps == scissors:
    print("당신이 이겼어요")
elif yourrps == "2" and pcrps == paper:
    print("당신이 졌어요")
#내가 보 - 비김 제외
elif yourrps == "3" and pcrps == scissors:
    print("당신이 졌어요")
elif yourrps == "3" and pcrps == rock:
    print("당신이 이겼어요")



#