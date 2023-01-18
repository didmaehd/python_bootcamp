

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

inputnumber = input("Where do you want to put the treasure? ")

x = inputnumber[0]
y = inputnumber[1]

map[int(y)-1][int(x)-1] = "X "
print(f"{row1}\n{row2}\n{row3}")