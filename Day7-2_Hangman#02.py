#행맨 프로젝트 1일차 / 랜덤 단어와 유저 선택 알파베을 확인하여 옳은지 틀린지 확인한다.

import random

#Step 2

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Word is {chosen_word}.")

#TODO 2-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#랜덤하게 선택된 단어를 _ 로 표현한다
world_length = len(chosen_word)
display = ["_"] * world_length
print(display)

guess = input("Guess a letter : ").lower()

#TODO 2-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#유저가 선택한 알파벳이, 랜덤하게 선택된 단어에 있으면 그 알파벳만 표기하고 프린트 한다

for position in range(world_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    else :
        pass

#TODO 2-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)


