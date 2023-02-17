#나름대로 가다듬기
#함수 두개로 합치기

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text,shift_aamount):
    result = ""
    for i in range(len(text)):
        replace_position = alphabet.index(text[i]) + shift_aamount
        if start_text == "decode":
            replace_position = alphabet.index(text[i]) - shift_aamount
        replace_text = alphabet[replace_position]
        result += replace_text
    print(result)
    print(f"The {direction}d text is [{result}].")

caesar(direction,shift)



