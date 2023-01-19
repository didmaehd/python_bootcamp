import random
#조금 더 깔끔하게 정리 해봄
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
game_image = [rock,paper,scissors]

#유저 선택을 숫자로 받고 이미지 출력
user_choice = int(input("What do you choose? Tyoe 0 for Rock, Type 1 for paper, Type 2 for scissor : \n"))
# user_choice = int(user_choice)
if user_choice >= 3 or user_choice < 0 :
    print("당신이 졌습니다. 0,1,2 중 선택하세요")
else :
    print(game_image[user_choice])
    #컴퓨터 선택 숫자로 받고 이미지 출력
    computer_choice = random.randint(0,2)
    print (game_image[computer_choice])

#각 조건 설정
#비김 조건
    if user_choice == computer_choice:
        print("비겼습니다. 한판 더 하시죠!")
    #내가 크면 이기는 조건 2개 와 예외 1개
    #예외를 위로 올려줘야 코드를 탈 수 있는 점!
    elif user_choice == 2 and computer_choice == 0:
        print("제가 이겼네요. 당신은 제 상대가 아닙니다.")
    elif user_choice > computer_choice:
        print("당신이 이겼습니다. 분하네요!")
    # 내가 작을경우의 패배2개와 예외 1개
    elif user_choice == 0 and  computer_choice == 2:
        print("당신이 이겼습니다. 분하네요!")
    elif user_choice < computer_choice:
        print("제가 이겼네요. 당신은 제 상대가 아닙니다.")
