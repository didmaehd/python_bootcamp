import random
import hangman_art
import hangman_word

print ("--------------------------\nWelcome to the Hangmang Game!")
print (hangman_art.logo)

word_list = hangman_word.word_list
chosen_word = random.choice(word_list)

#test code : 선택된 단어를 미리 알려줌
# print(f"Pssst, the solution is {chosen_word}.")

# 자주 사용하는 선택된 단어의 길이를 변수로 저장 해둠
word_length = len(chosen_word)

# 선택된 단어의 알파벳 수만큼 _ 로 리스트 생성 , 출력
display = ["_"] * word_length
print(display)

# 오답시 줄어들 생명력 셋팅
lives = 6

#게임 종료시 while문을 종료시키기위한 변수 설정
end_game = False
#end_game이 true이면 while문을 실행
while not end_game :
    # 유저로부터 문자를 입력 받고 소문자로 변환
    guess = input("Guess a letter : ").lower()
    #입력 받은 문자가 이미 display에 있다면 , 이미 입력한 단어라고 알려줌
    if guess in display:
        print(f"You have already guessed [{guess}]")
    #단어의 길이만큼 for문 실행 순차적으로 실행
    for position in range(word_length):
        #letter 변수는 선택된 단어의 position값으로 지정
        letter = chosen_word[position]
        #letter 변수와 유저 추측값을 비교헤서 같으면 display에 저장
        if letter == guess:
            display[position] = letter

    # 추측 값이 선택된 단어에 없다면 , 생명력을 1 차감하고 메세지 출력
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed [{guess}], that's not in the word. You lose a life")
        print(f"Your life are left {lives}")
        #만약 생명력이 0이면 end_game을 True로 바꿔주고 게임을 종료, 죽었다고 메세지 출력
        if lives == 0:
            end_game = True
            print("You Die!")
            print(f"The word is {chosen_word}.")
    print (f"{' '.join(display)}")

    # display에 더이상 _ 가 없다면 end_game 값을 True로 바꿔주고 게임 종료, 이겼다는 메세지 출력
    if "_" not in display:
        end_game = True
        print("You win!")
    # 생명력 수만큼 ASCII ART 출력
    print(hangman_art.stages[lives])

