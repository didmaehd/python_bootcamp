#leap year check

#윤년의 조건
#서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다. (1988년, 1992년)
#서력 기원 연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다. (1700년, 1800년, 1900년, 2100년, 2200년, 2300년...)
#서력 기원 연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다. (1600년, 2000년, 2400년...)


# check_year = int(input("Which year do you want to check leap year?  "))
# if check_year % 4 == 0:
#     if check_year % 100 == 0 and check_year % 400 == 0:
#         print ("leap year")
#     elif check_year % 100 == 0 :
#         print ("not leap year")
#     else :
#         print ("leap year")
# else :
#     print ("not leap year")


year = int(input("Which year do you want to check? :"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  