import random


# #random.choice를 사용할 경우
names_input = input("Give me everybody's name, seperated by a comma. \n")
names = names_input.split(",")
result = random.choice(names)
print(f"당첨자는{result}입니다 ")

#random choice를 사용하지 않을 경우
names = input("Give me everybody's name, seperated by a comma. \n")
names_split = names.split(",")


names_list_len = len(names_split)
selected_number = random.randint(0,names_list_len-1)
selected_person = names_split[selected_number]
print(f"당청자는 {selected_person} 입니다")