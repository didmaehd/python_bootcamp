
# shift = 4
# text = ("a3$#$b c")
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

# cipher = ""
# for i in text:
#     if i not in alphabet:
#         cipher += i
#     elif  i in alphabet:
#         position = alphabet.index(i)
#         new_position = position + shift
#         cipher += alphabet[new_position]
# print(cipher)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = 1318
if i > 25 :
    i = i % 25
print(alphabet[i])


# end_game = False
# while not end_game:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     def caesar(start_text,shift_amount,cipher_direction):
#         end_text = ""
#         if cipher_direction == "decode":
#             shift_amount = shift_amount * -1
#         for letter in start_text:
#             if letter not in alphabet:
#                 end_text += letter
#             elif letter in alphabet:
#                 position = alphabet.index(letter)
#                 new_position = position + shift_amount
#                 end_text += alphabet[new_position]
#         print(end_text)
#         print(f"The {cipher_direction}d text is [{end_text}].")

#     caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

#     retry = input("Type 'yes' if you want to go again, Otherwise type 'no' : ")
#     if retry == "yes":
#         end_game = False
#     elif retry == "no":
#         end_game = True