# 복수의 점수를 input 함수로 받는다
# int로 변환 시킨다

scores = input("Enter Scores : ").split(" ")

for n in range(0,len(scores)): #range는 마지막 값을 포함하지 않는다
    scores[n] = int(scores[n])

#받은 점수중 가장 높은 점수를 출력한다
#max 함수는 사용하지 않는다
max_score = 0
for n in scores:
    if n > max_score :
        max_score = n
print(f"가장 높은 점수는 {max_score}점 입니다.")


