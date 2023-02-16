#나이를 입력하면 남은 삶을 일, 주, 시간으로 알려주는 코드
#90세까지 사는것으로 가정한다


# 나이 inout

age = input("How old are you? ")
left_years = 90 - int(age)

left_months = left_years * 12
left_weeks = left_years * 52
left_days = left_years * 365

print(f"You have {left_years} years, {left_months} months, {left_weeks} weeks, {left_days} days left.")