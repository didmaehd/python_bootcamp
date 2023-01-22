# 패스워드 생성기 만들기


import random
#문자열, 숫자 , 기호 리스트를 생성한다
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print ("Welcom to the PyPassword Generator!")
#input 받을 문구를 생성한다
n_letters = int(input("How many letters would you like in your password? : "))
n_symbols = int(input("How many symbols would you like? : "))
n_numbers = int(input("How many numbers would you like? : "))

#랜덤 요소를 더해줄 빈 변수를 생성한다.
#첨부터 섞을 목적이면 리스트를 만들어서 랜덤한 값을 받앚면 좋다
sample_password = ""
#유저가 요청한 길이만큼 문자열, 기호, 숫자를 랜덤하게 생성하여 미리 준비한 빈 변수에 넣는다
for letter in range(0,n_letters):
    sample_password += random.choice(letters)

for symbol in range(0,n_symbols):
    sample_password += random.choice(symbols)

for number in range(0,n_numbers):
    sample_password += random.choice(numbers)

#단순 나열 패스워드 생성 완성
print(sample_password) 

# 단순 나열 패스워드를 섞어보자

#단순 나열 패스워드 변수를 리스트로 변경
list_password = list(sample_password)
# print(list_password)

# 리스트에 담긴 문자열을 랜덤하게 섞어준다
random.shuffle(list_password)
# print(list_password)

# 섞어진 리스트를 다시 일반 변수로 변환하여 최종 패스워드 완성
password = "".join(list_password)
print(password)


#한번에 섞는것까지 구현하기


d_password = []         #랜덤 값을 받을 빈 리스트 생성
for letter in range(0,n_letters):
    d_password += random.choice(letters)

for symbol in range(0,n_symbols):
    d_password += random.choice(symbols)

for number in range(0,n_numbers):
    d_password += random.choice(numbers)

random.shuffle(d_password) # 받은 랜덤 값을 섞어준다
print(d_password)
#for문으로 리스트를 일반 뱐수로 바꿔줄수 있다
f_password = ""
for char in d_password:
    f_password += char
# d_password = "".join(d_password) #리스트를 일반 변수로 간단하게 바꿔주는 방법도 있다.
print(f_password)


