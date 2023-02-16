import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Word is {chosen_word}.")

world_length = len(chosen_word)

display = ["_"] * world_length
print(display)


#TODO 3-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

end_game = False
while not end_game :
    guess = input("Guess a letter : ").lower()
    for position in range(world_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_game = True
        print("You win!")




    