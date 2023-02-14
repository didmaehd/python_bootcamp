#피즈버즈 게임


#일단 만들기 : 조건 : 3으로 나눠 떨어지면 피즈, 5로 나눠 떨어지면 버즈, 3,5로 나눠 떨어지면 피즈버즈
#for 문으로 100까지 돌려봄

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0 :
#         print("FIZZBUZZ")
#     elif i % 3 == 0 :
#         print("FIZZ")
#     elif i % 5 == 0 :
#         print ("BUZZ")
#     else :
#         print(i)

#버그 수정하기
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # or -> amd로 변경
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)