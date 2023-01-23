#행맨 프로젝트 1일차 / 랜덤 단어와 유저 선택 알파베을 확인하여 옳은지 틀린지 확인한다.

import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess word : ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


#변수에서 단어 하나씩 추출할수 있는지 모르고 리스트로 변환해서 하나씩 대입 비교 한 경우
# chosen_word_list = list(chosen_word)
# a = 0
# for a in range(0,len(chosen_word_list)):
#     if guess == chosen_word_list[a]:
#         print("Right")
#     else :
#         print("Wrong")
#         a += 1
# print("-----")

#변수의 각 알파벳과 입력값을 비교한 경우
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else :
        print("Wrong")
