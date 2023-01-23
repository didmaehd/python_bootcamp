alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(pline_text,shift_aamount):
    cipher = ""
    for i in range(len(pline_text)):
        replace_position = alphabet.index(pline_text[i]) + shift_aamount
        replace_text = alphabet[replace_position]
        cipher = cipher + replace_text
    print(cipher)
    print(f"Cipher text is [{cipher}].")

def decrypt(pline_text,shift_aamount):
    decoded_text = ""
    for i in range(len(pline_text)):
        replace_position = alphabet.index(pline_text[i]) - shift_aamount
        replace_text = alphabet[replace_position]
        decoded_text = decoded_text + replace_text
    print(decoded_text)
    print(f"Dcoded text is [{decoded_text}].")
 
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)

