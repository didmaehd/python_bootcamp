alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#암호화 함수 생성
def encrypt(pline_text,shift_aamount):
    #암호화한 텍스트를 담을 빈 변수 생성
    cipher = ""
    #입력받은 텍스트의 길이만큼 실행
    for i in range(len(pline_text)):
        #암호화할 텍스트의 위치에 이동시킬 위치를 더해줌
        replace_position = alphabet.index(pline_text[i]) + shift_aamount
        #이동 시킨 위치의 텍스트룰 찾고
        replace_text = alphabet[replace_position]
        #찾은 텍스트를 위에서 생선한 암화화된 텍스트를 담을 빈 변수에 for문이 돌 동안 하나씩 넣어줌
        cipher += replace_text
    #암호화가 완료된 텍스트 출력
    print(cipher)
    print(f"Cipher text is [{cipher}].")

#복호화 함수 생성
def decrypt(pline_text,shift_aamount):
    #복호화 텍스트를 담을 빈 변수 생성
    decoded_text = ""
    for i in range(len(pline_text)):
        #복호화할 텍스트 위치에서 이동시킬 위치를 빼줌
        replace_position = alphabet.index(pline_text[i]) - shift_aamount
        #이동 시킨 위치의 텍스트를 찾고
        replace_text = alphabet[replace_position]
        #for문이 실핼 될 동안 찾은 알파벳을 위에서 생성한 복호화 텍스트를 담을 빈 변수에 하나씩 넣어 줌
        decoded_text = decoded_text + replace_text
    #최종적으로 복호화된 텍스트 출력    
    print(decoded_text)
    print(f"Dcoded text is [{decoded_text}].")

#선택한 direction에 따라 호출할 함수 선택 
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else :
    print("Please restart this program and type 'encode' or 'decode.'")
    


