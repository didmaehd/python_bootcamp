#1부터 100까지 숫자중에 짝수만 합하기

#for + if문 사용
total_even = 0
for number in range(1,101):
    if number % 2 == 0:
        total_even += number
print(total_even)


#for문만 사용
total = 0
for n in range(2,101,2): #2부터 100까지 2단계
    total += n
print(total)