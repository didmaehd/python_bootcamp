############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 21): #range가 20이면 19까지만 실행되기때문에 21로 수정
#     if i == 20: 
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5) # list 범위 벗아났기에 수정
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: # 1994년의 경우 어떤 output도 받을수 없기에 = 추가
#   print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you? ")) # int로 변경
# if age > 18:
#   print(f"You can drive at age {age}.") #들여쓰기 수정 + f string 수정

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # == 을 =로 수정
# # a = 1 a는1이다 . a == 1 a는 1과 같다 - 불리언
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])