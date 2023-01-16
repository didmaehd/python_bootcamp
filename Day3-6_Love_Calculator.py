


# name1과 name2를 input 받아요
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#name1과 name2를 소문자 처리하고 둘을 합한다
lower_name1 = name1.lower()
lower_name2 = name2.lower()
full_name = lower_name1 + lower_name2


#합친 이름에서 true love의 알파벳수를 추출한다
true_point = 0
true_point = true_point + full_name.count("t")
true_point = true_point + full_name.count("r")
true_point = true_point + full_name.count("u")
true_point = true_point + full_name.count("e")

love_point = 0
love_point = love_point + full_name.count("l")
love_point = love_point + full_name.count("o")
love_point = love_point + full_name.count("v")
love_point = love_point + full_name.count("e")

#추출한 수를 스트링으로 변환하여 더하고 , 다시 정수로 변환한다
# result = str(true_point) + str(love_point)
# int_result = int(result)
int_result = int(str(true_point) + str(love_point))

#합한 결과에따라 아래 구문이 나오도록 if문을 만든다
if int_result < 10 and int_result > 90:
    print(f"Your score is {int_result}, you go together like coke and mentos.")
elif int_result in range(40,50):
    print(f"Your score is {int_result}, you are alright together.")
else :
    print(f"Your score is {int_result}")
