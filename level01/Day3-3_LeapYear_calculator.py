#4로 나눠 나머지가 없으면 윤뇬
##4로나눠 나머지가 없더라도 100으로 나눠서 나머지가 없으면 윤년이 아님
###100으로 니눠 나머지가 없더라도 400으로 나눠 나머지가 없으면 윤년

year = int(input("Enter year : "))
# if year % 4 == 0 and year % 100 != 0:
#     print(f"{year}년은 윤년입니다")
# elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
#     print(f"{year}년은 윤년이 아닙니다")
# elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print(f"{year}년은 윤년입니다")
# else :
#     print(f"{year}년은 윤년입니다")


if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print(f"{year}년은 윤년입니다")
        else :
            print(f"{year}년은 윤년이 아닙니다")
    else :
        print(f"{year}년은 윤년입니다")
else :
    print(f"{year}년은 윤년이 아닙니다")
    